import requests
import csv
import re
import os
from bs4 import BeautifulSoup

from constants import BASE_VNL_URL, YEAR, SEX, DATA_DIR, RAW_DATA_FILE_EXTENSION
    
teams_url = f"{BASE_VNL_URL}/{YEAR}/teams/{SEX}/?"
headers = {"User-Agent": "Mozilla/5.0"}
teams = []

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

html = requests.get(teams_url, headers=headers)
html.encoding = 'utf-8'  # Set the encoding to UTF-8
soup = BeautifulSoup(html.text, "html.parser")

for a in soup.select('a[href*="/teams/"]'):
    name = a.get_text(strip=True)

    if name in ["Teams", "Men's", "Women's"]:
        continue
    if name not in teams:
        teams.append(name)

with open(f"{DATA_DIR}/teams{RAW_DATA_FILE_EXTENSION}", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Country", "Code"])

    for team in teams:
        match = re.match(r"(.+?)([A-Z]{3})$", team)

        if match:
            country = match.group(1).strip()
            code = match.group(2)
            writer.writerow([country, code])

print("Teams scraped successfully!")
print(teams)