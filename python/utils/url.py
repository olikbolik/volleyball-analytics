
from python.utils.logger import logger
from python.utils.constants import BASE_VNL_URL, CURRENT_YEAR


def generate_teams_url(year: str, sex: str) -> str:
    """ Generates the URL for scraping teams based on the provided year. """
    if year == CURRENT_YEAR:
        return f"{BASE_VNL_URL}/teams/{sex}/?"
    else:
        return f"{BASE_VNL_URL}/{year}/teams/{sex}/?"
#teams 
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/teams/women/?
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/teams/women/?

#players
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2025/teams/women/7535/players/?

#team_stats
    # https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/teams/women/
