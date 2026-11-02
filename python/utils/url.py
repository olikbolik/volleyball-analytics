
from python.utils.logger import logger
from python.utils.constants import BASE_VNL_URL, CURRENT_YEAR
from python.utils.constants import STATISTICS


def generate_teams_url(year: str, sex: str) -> str:
    """ Generates the URL for scraping teams based on the provided year. """
    if year == CURRENT_YEAR:
        return f"{BASE_VNL_URL}/teams/{sex}/?"
    else:
        return f"{BASE_VNL_URL}/{year}/teams/{sex}/?"
#teams 
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/teams/women/?
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/teams/women/?


def generate_statistics_url(year: str, sex: str) -> str:
    """ Generates the URL for scraping statistics based on the provided year and sex. """
    if year == CURRENT_YEAR:
        for metric in STATISTICS:
            yield (metric, f"{BASE_VNL_URL}/statistics/{sex}/{metric}/?")
    else:
        for metric in STATISTICS:
            yield (metric, f"{BASE_VNL_URL}/{year}/statistics/{sex}/{metric}/?")
#team_stats
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/statistics/women/
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/statistics/women/best-attackers/?


def generate_finals_statistics_url(year: str, sex: str) -> str:
    """ Generates the URL for scraping finals statistics based on the provided year and sex. """
    if year == CURRENT_YEAR:
        for metric in STATISTICS:
            yield (metric, f"{BASE_VNL_URL}/finals-statistics/{sex}/{metric}/?")
    else:
        for metric in STATISTICS:
            yield (metric, f"{BASE_VNL_URL}/{year}/finals-statistics/{sex}/{metric}/?")
#team_stats
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/finals-statistics/men/best-scorers/?




#players
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/teams/women/7535/players/?

