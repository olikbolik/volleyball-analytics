from logger import logger


def is_valid_year(year: str) -> bool:
    """ Validates if the provided year is a valid 4-digit year. """
    
    logger.debug(f"Validating year: {year}")
    if not year.isdigit() or len(year) != 4:
        logger.error(f"Invalid year format: {year}. Please provide a valid 4-digit year.")
        return False
    return True

