import requests
import csv
import re
import os
import sys
from bs4 import BeautifulSoup

from logger import logger
from utils.file_util import directory_exists, create_directory
from utils.validation import is_valid_year, validate_arguments
from utils.url import generate_teams_url
from constants import CURRENT_YEAR, DATA_DIR, RAW_DATA_FILE_EXTENSION
    
data_to_scrape = "teams"
headers = {"User-Agent": "Mozilla/5.0"}


# function for scraping teams by year 
def scrape_teams(year: str=CURRENT_YEAR, sex: str="women"):
    """ Scrapes the teams for the given year and sex and saves them to a CSV file. """
    teams_url = generate_teams_url(year, sex)
    logger.debug(f"Scraping teams for {year} from {teams_url}")

    try:
        logger.debug(f"Sending GET request to {teams_url}")
        html = requests.get(teams_url, headers=headers)
        html.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred while fetching data for year {year}: {e}")
        return
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data for year {year}: {e}")
        return

    html.encoding = 'utf-8'  # Set the encoding to UTF-8
    teams = parse_team_names(html.text)  # Call the function to parse team names

    # Check if the teams directory exists, and create it if it doesn't
    teams_dir = check_and_create_teams_directory(year, sex, data_to_scrape)
    teams_file_path = f"{teams_dir}/teams_{year}_{sex}{RAW_DATA_FILE_EXTENSION}"

    write_teams_to_csv(teams, teams_file_path)  # Call the function to write teams to CSV



def parse_team_names(html_content: str) -> list:
    """ Parses the HTML content to extract team names. """
    soup = BeautifulSoup(html_content, "html.parser")
    teams = []

    for a in soup.select('a[href*="/teams/"]'):
        name = a.get_text(strip=True)
        if name in ["Teams", "Men's", "Women's"]:
            continue
        if name not in teams:
            teams.append(name)
    return teams


def check_and_create_teams_directory(year: str, sex: str, data_to_scrape: str) -> str:
    """ Checks if the teams directory exists, and creates it if it doesn't. """
    teams_dir = f"{DATA_DIR}/{sex}/{year}/{data_to_scrape}"
    logger.debug(f"Checking if teams directory exists at {teams_dir}...")

    if not directory_exists(teams_dir):
        logger.debug(f"Teams directory does not exist. Creating directory at {teams_dir}")
        create_directory(teams_dir)
        logger.debug(f"Teams directory created at {teams_dir}.")
    return teams_dir


def write_teams_to_csv(teams: list, teams_file_path: str) -> None:
    """ Writes the list of teams to a CSV file. """
    logger.debug(f"Writing teams data to {teams_file_path}...")

    with open(teams_file_path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["Country", "Code"])

        for team in teams:
            match = re.match(r"(.+?)([A-Z]{3})$", team)

            if match:
                country = match.group(1).strip()
                code = match.group(2)
                writer.writerow([country, code])

    logger.debug(f"Teams: {teams} written to {teams_file_path}.")



# function to validate arguments
years_to_scrape, gender_to_scrape = validate_arguments(sys.argv)

for year in years_to_scrape:
    logger.info(f"Fetching {gender_to_scrape} teams for year {year}...")
    scrape_teams(year, gender_to_scrape)
    logger.info(f"Fetched {gender_to_scrape} teams for {year} year successfully.")

