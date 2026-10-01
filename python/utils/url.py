
from logger import logger
from constants import BASE_VNL_URL, CURRENT_YEAR, SEX


def generate_teams_url(year: str) -> str:
    """ Generates the URL for scraping teams based on the provided year. """
    if year == CURRENT_YEAR:
        return f"{BASE_VNL_URL}/teams/{SEX}/?"
    else:
        return f"{BASE_VNL_URL}/{year}/teams/{SEX}/?"
teams 
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/teams/women/?
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/teams/women/?

players
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/teams/women/7535/players/?

team_stats
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/teams/women/
