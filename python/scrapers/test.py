import requests
import csv
import re
import os, sys
from bs4 import BeautifulSoup

from utils.validation import is_valid_year
from constants import BASE_VNL_URL, CURRENT_YEAR, SEX, DATA_DIR, RAW_DATA_FILE_EXTENSION
from logger import logger
    
teams_url = f"{BASE_VNL_URL}/{CURRENT_YEAR}/teams/{SEX}/?"
headers = {"User-Agent": "Mozilla/5.0"}
teams = []
logger.info(f"Scraping teams for {CURRENT_YEAR} from {teams_url}")
for arg in sys.argv:
    print(arg)

def test(year: str=CURRENT_YEAR):
    if not is_valid_year(year):
        return

    if year == CURRENT_YEAR:
        teams_url = f"{BASE_VNL_URL}/teams/{SEX}/?"
    else:
        teams_url = f"{BASE_VNL_URL}/{year}/teams/{SEX}/?"
    logger.info(f"Scraping teams for {year} from {teams_url}")
