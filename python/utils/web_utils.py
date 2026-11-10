import pandas as pd
from python.utils.logger import logger


def fetch_html(url: str) -> str:
    """ Fetches the HTML content from the given URL. """
    try:
        logger.debug(f"Sending GET request to {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        response.encoding = 'utf-8'  # Set the encoding to UTF-8
        return response.text
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred while fetching data from {url}: {e}")
        return ""
    except requests.exceptions.RequestException as e:
        logger.error(f"Error occurred while fetching data from {url}: {e}")
        return ""


def fetch_html_with_tables(url: str) -> tuple:
    """ Fetches the HTML content and tables from the given URL. """
    try:
        logger.debug(f"Sending GET request to {url}")
        tables = pd.read_html(url)
        return response.text, tables
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred while fetching data from {url}: {e}")
        return "", []
    except requests.exceptions.RequestException as e:
        logger.error(f"Error occurred while fetching data from {url}: {e}")
        return "", []
    except ValueError as e:
        logger.error(f"No tables found at {url}: {e}")
        return response.text, []
