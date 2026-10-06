# previous years
# https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/statistics/women/best-scorers/?
# current year
# https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/statistics/women/best-scorers/?


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR/"data"
RAW_DATA_FILE_EXTENSION = ".csv"

BASE_VNL_URL = "https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league"
CURRENT_YEAR = "2026"
SEX_FEMALE = "women"
SEX_MALE = "men"
STATISTICS = ["best-scorers", "best-attackers", "best-blockers", "best-servers", "best-setters", "best-diggers", "best-receivers"]
