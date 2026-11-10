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
#stats
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/statistics/women/
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/statistics/women/best-attackers/?
    # https://en.volleyballworld.com/volleyball/world-ranking/men?

def generate_finals_statistics_url(year: str, sex: str) -> str:
    """ Generates the URL for scraping finals statistics based on the provided year and sex. """
    if year == CURRENT_YEAR:
        for metric in STATISTICS:
            yield (metric, f"{BASE_VNL_URL}/finals-statistics/{sex}/{metric}/?")
    else:
        for metric in STATISTICS:
            yield (metric, f"{BASE_VNL_URL}/{year}/finals-statistics/{sex}/{metric}/?")
#finals_stats
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/finals-statistics/men/best-scorers/?
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/finals-statistics/men/best-scorers/?


def generate_players_url(year: str, sex: str, team_id: int) -> str:
    """ Generates the URL for scraping players based on the provided year, sex, and team ID. """
    if year == CURRENT_YEAR:
        return f"{BASE_VNL_URL}/teams/{sex}/{team_id}/players/?"
    else:
        return f"{BASE_VNL_URL}/{year}/teams/{sex}/{team_id}/players/?"
#players
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/teams/women/7535/players/?
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/teams/women/7535/players/?

