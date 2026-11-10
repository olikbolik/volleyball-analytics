import requests
import csv
import re
import sys
from bs4 import BeautifulSoup

from python.utils.logger import logger
from python.utils.file_util import directory_exists, create_directory, build_directory_path
from python.utils.validation import validate_arguments
from python.utils.url import generate_teams_url, generate_players_url
from python.utils.web_utils import fetch_html
from python.utils.constants import CURRENT_YEAR, SEX_FEMALE, DATA_DIR, RAW_DATA_FILE_EXTENSION
    
data_to_scrape = ["teams", "players"]
headers = {"User-Agent": "Mozilla/5.0"}


def scrape_teams(year: str=CURRENT_YEAR, sex: str=SEX_FEMALE) -> None:
    """ Scrapes teams and players for the given year and sex and saves them to a CSV file. """

    teams = scrape_teams_info(year, sex)
    if not teams:
        logger.error(f"No teams found for {sex} in {year}.")
        return
    
    # Check if the teams directory exists, and create it if it doesn't
    teams_dir = check_and_create_teams_directory(year, sex, data_to_scrape[0])
    write_teams_to_csv(teams, teams_dir, year, sex)  # Call the function to write teams to CSV

    players = scrape_players_info(year, sex)
    players_dir = check_and_create_players_directory(year, sex, data_to_scrape[1])
    write_players_to_csv(players, players_dir, year, sex)  # Call the function to write players to CSV 


def scrape_teams_info(year: str, sex: str) -> list:
    teams_url = generate_teams_url(year, sex)
    logger.debug(f"Scraping teams for {year} from {teams_url}")
    teams_html = fetch_html(teams_url)

    if not teams_html:
        logger.error(f"Failed to fetch {sex} teams data for {year}")
        return []

    return parse_teams_data(teams_html.text)


def parse_teams_data(html_content: str) -> list:
    """ Parses the HTML content to extract team data. """
    soup = BeautifulSoup(html_content, "html.parser")
    teams = []

    for a in soup.select('a[href*="/teams/"]'):
        name = a.get_text(strip=True)
        link = a.get("href", "")
        if name in ["Teams", "Men's", "Women's"]:
            continue
        else:
            name_match = re.match(r"(.+?)([A-Z]{3})$", name)
            id_match = re.search(r"/teams/women/(\d+)/schedule/", link)
            country = name_match.group(1).strip()
            code = name_match.group(2)
            team_id = id_match.group(1)
            if name_match and id_match:
                teams.append((country, code, team_id))
    return teams


def check_and_create_teams_directory(year: str, sex: str) -> Path:
    """ Checks if the teams directory exists, and creates it if it doesn't. """
    # teams_dir = f"{DATA_DIR}/{sex}/{year}/{data_to_scrape}"
    teams_dir = build_directory_path(sex, year, data_to_scrape)

    if not directory_exists(teams_dir):
        logger.debug(f"Teams directory does not exist.")
        create_directory(teams_dir)
    return teams_dir


def write_teams_to_csv(teams: list, teams_dir: Path, year: str, sex: str) -> None:
    """ Writes the list of teams to a CSV file. """
    teams_file_path = f"{teams_dir}/teams_{year}_{sex}{RAW_DATA_FILE_EXTENSION}"
    logger.debug(f"Writing teams data to {teams_file_path}...")


    with open(teams_file_path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["Country", "Code", "ID"])

        writer.writerows(teams)

    logger.debug(f"Teams written to {teams_file_path}.")


def scrape_players_info(year: str=CURRENT_YEAR, sex: str=SEX_FEMALE) -> None:
    """ Scrapes the players for the given year, sex and teams and saves them to a CSV file. """
    pass  # Placeholder for the actual implementation of scraping players info


def write_players_to_csv(players: list, players_dir: Path, year: str, sex: str) -> None:
    pass


# function to validate arguments
years_to_scrape, gender_to_scrape = validate_arguments(sys.argv)

for year in years_to_scrape:
    logger.info(f"Fetching {gender_to_scrape} teams for year {year}...")
    scrape_teams(year, gender_to_scrape)
    logger.info(f"Fetched {gender_to_scrape} teams for {year} year successfully.")
