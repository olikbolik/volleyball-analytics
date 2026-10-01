import requests
import csv
import re
import os
import sys
from bs4 import BeautifulSoup

from logger import logger
from utils.file_util import directory_exists, create_directory
from utils.validation import is_valid_year
from constants import BASE_VNL_URL, CURRENT_YEAR, SEX, DATA_DIR, RAW_DATA_FILE_EXTENSION
    
teams_dir = f"{DATA_DIR}/teams"
headers = {"User-Agent": "Mozilla/5.0"}
teams = []


# function for scraping teams by year 
def scrape_teams(year: str=CURRENT_YEAR):
    """ Scrapes the teams for the given year and saves them to a CSV file. """
    if not is_valid_year(year):
        return

    teams_url = generate_teams_url(year)
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
    soup = BeautifulSoup(html.text, "html.parser")

    for a in soup.select('a[href*="/teams/"]'):
        name = a.get_text(strip=True)

        if name in ["Teams", "Men's", "Women's"]:
            continue
        if name not in teams:
            teams.append(name)

    # Check if the teams directory exists, and create it if it doesn't
    check_and_create_teams_directory(teams_dir)

    with open(f"{teams_dir}/teams_{year}{RAW_DATA_FILE_EXTENSION}", "w", newline="", encoding="utf-8-sig") as file:
        logger.debug(f"Writing teams data to {teams_dir}/teams_{year}{RAW_DATA_FILE_EXTENSION}")
        writer = csv.writer(file)
        writer.writerow(["Country", "Code"])

        for team in teams:
            match = re.match(r"(.+?)([A-Z]{3})$", team)

            if match:
                country = match.group(1).strip()
                code = match.group(2)
                writer.writerow([country, code])

    logger.info(f"Teams for {year} scraped successfully!")
    logger.debug(f"Teams: {teams} written to {teams_dir}/teams_{year}{RAW_DATA_FILE_EXTENSION}")


def check_and_create_teams_directory(teams_dir):
    """ Checks if the teams directory exists, and creates it if it doesn't. """
    logger.debug(f"Checking if teams directory exists at {teams_dir}")

    if not directory_exists(teams_dir):
        logger.debug(f"Teams directory does not exist. Creating directory at {teams_dir}")
        create_directory(teams_dir)




if len(sys.argv) <= 1:
   logger.warning("No arguments were given")
   logger.debug("Fetching teams for the current year...")
   scrape_teams(CURRENT_YEAR)
   logger.debug(f"Fetched teams for {CURRENT_YEAR} successfully")

else:
    logger.info(f"Arguments received: {sys.argv[1:]}")
    #https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/teams/women/?
    #https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/teams/women/?

    for arg in sys.argv[1:]:
        logger.debug(f"Fetching teams for year {arg}...")
        scrape_teams(arg)
        logger.debug(f"Fetched teams for {arg} successfully")

