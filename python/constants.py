# previous years
# https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/statistics/women/best-scorers/?
# current year
# https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/statistics/women/best-scorers/?


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR/"data"
BASE_VNL_URL = "https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league"
YEAR = "2025"
SEX = "women"
STATISTICS = ["best-scorers", "best-attackers", "best-blockers", "best-servers", "best-setters", "best-diggers", "best-receivers"]
RAW_DATA_FILE_EXTENSION = ".csv"
