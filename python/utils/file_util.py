from pathlib import Path, mkdir, exists

from python.utils.logger import logger
from python.utils.constants import DATA_DIR


def directory_exists(directory_path: Path) -> bool:
    logger.debug(f"Checking if directory exists at {directory_path}")
    directory_exists = directory_path.exists()
    if directory_exists:
        logger.debug(f"Directory exists at {directory_path}")
        return True
    logger.debug(f"Directory does not exist at {directory_path}")
    return False


def create_directory(directory_path: Path) -> None:
    logger.info(f"Creating directory at {directory_path}") 
    try:
        directory_path.mkdir(parents=True, exist_ok=True) 
        logger.info(f"Directory successfully created at {directory_path}")
    except FileExistsError:
        logger.error(f"Error: the '{directory_path}' path already exists.")
    except FileNotFoundError:
        logger.error(f"Error: '{directory_path}' misses required parent folder(s).")
    except OSError:
        logger.error(f"Error: path invalid or general system I/O error.")


def build_directory_path(sex: str, year: str, data_to_scrape: str) -> Path:
    """ Builds the directory path for the given sex, year, and data to scrape. """
    logger.debug(f"Building directory path for sex: {sex}, year: {year}, data_to_scrape: {data_to_scrape}")
    return DATA_DIR/ sex / year / data_to_scrape
