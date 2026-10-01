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


# function for scraping team stats by year 
def scrape_team_stats(year: str=CURRENT_YEAR):
    if not is_valid_year(year):
        return

    if year == CURRENT_YEAR:
        teams_url = f"{BASE_VNL_URL}/teams/{SEX}/?"
    else:
        teams_url = f"{BASE_VNL_URL}/{year}/teams/{SEX}/?"
    logger.info(f"Scraping teams for {year} from {teams_url}")

    try:
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

    with open(f"{teams_dir}/teams_{year}{RAW_DATA_FILE_EXTENSION}", "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["Country", "Code"])

        for team in teams:
            match = re.match(r"(.+?)([A-Z]{3})$", team)

            if match:
                country = match.group(1).strip()
                code = match.group(2)
                writer.writerow([country, code])

    print(f"Teams for {year} scraped successfully!")
    #print(teams)



# Create the directory for teams if it doesn't exist
def check_and_create_teams_directory(teams_dir):
    logger.debug(f"Checking if teams directory exists at {teams_dir}")

    if not directory_exists(teams_dir):
        logger.debug(f"Teams directory does not exist. Creating directory at {teams_dir}")
        create_directory(teams_dir)



check_and_create_teams_directory(teams_dir)

if len(sys.argv) <= 1:
   logger.warning("No arguments were given")
   logger.debug("Fetching teams for the current year...")
   scrape_team_stats(CURRENT_YEAR)

else:
    logger.info(f"Arguments received: {sys.argv[1:]}")
    #https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/teams/women/?
    #https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/teams/women/?

    for arg in sys.argv[1:]:
        logger.debug(f"Fetching teams for year {arg}...")
        scrape_team_stats(arg)
