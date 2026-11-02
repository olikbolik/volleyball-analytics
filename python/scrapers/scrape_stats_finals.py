import sys
import pandas as pd

from python.utils.logger import logger
from python.utils.file_util import directory_exists, create_directory
from python.utils.validation import validate_arguments
from python.utils.url import generate_finals_statistics_url
from python.utils.constants import CURRENT_YEAR, SEX_FEMALE, DATA_DIR, RAW_DATA_FILE_EXTENSION

#url = 'https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/finals-statistics/women/'
# https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/finals-statistics/women/best-scorers/?
data_to_scrape = "finals-statistics"


# function for scraping statistics by year 
def scrape_finals_statistics(year: str=CURRENT_YEAR, sex: str=SEX_FEMALE):
    """ Scrapes finalsstatistics for the given year and sex and saves them to a CSV file. """
    
    metrics_and_finals_stats_urls = generate_finals_statistics_url(year, sex)
    finals_stats_dir = check_and_create_finals_statistics_directory(year, sex, data_to_scrape)

    for metric, metric_url in metrics_and_finals_stats_urls:
        logger.debug(f"Scraping {metric} for year {year} from {metric_url}")

        try:
            tables = pd.read_html(metric_url)
            logger.info(f"{len(tables)} tables found for {metric}")
        except Exception as e:
            logger.error(f"No tables found, invalid url {metric_url}: {e}")  
            break  # Exit the loop if the URL is invalid
            # check next url
            # https://vnlw.volleystation.com/en/stat-rankings/
        else:
            if not tables:
                logger.warning(f"No tables found for {metric} at {metric_url}")
                continue
            df = tables[0]
            # Save the DataFrame to a CSV file
            write_finals_stats_to_csv(df, finals_stats_dir, metric, year, sex)
        finally:
            logger.info(f"Finished processing of metric {metric} for year {year}.")


def check_and_create_finals_statistics_directory(year: str, sex: str, data_to_scrape: str) -> str:
    """ Checks if the finalsstatistics directory exists, and creates it if it doesn't. """
    finals_statistics_dir = f"{DATA_DIR}/{sex}/{year}/{data_to_scrape}"
    
    if not directory_exists(finals_statistics_dir):
        logger.debug(f"Finals statistics directory does not exist for {year} and {sex}.")
        create_directory(finals_statistics_dir)
    return finals_statistics_dir


def write_finals_stats_to_csv(df: pd.DataFrame, finals_statistics_dir: str, metric: str, year: str, sex: str) -> None:
    raw_data_file = f"{finals_statistics_dir}/finals_statistics_{metric}_{year}_{sex}{RAW_DATA_FILE_EXTENSION}"
    df.to_csv(raw_data_file, index=False)
    logger.info(f"{metric} processed successfully.")


# function to validate arguments
years_to_scrape, gender_to_scrape = validate_arguments(sys.argv)

for year in years_to_scrape:
    logger.info(f"Fetching {gender_to_scrape} finals statistics for year {year}...")
    scrape_finals_statistics(year, gender_to_scrape)
    logger.info(f"Fetched {gender_to_scrape} finals statistics for {year} year successfully.")

