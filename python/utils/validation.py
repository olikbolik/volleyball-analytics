from logger import logger
from constants import CURRENT_YEAR, SEX_FEMALE, SEX_MALE


def is_valid_year(year: str) -> bool:
    """ Validates if the provided argument is a valid 4-digit year. """
    
    if not year.isdigit():
        return False
    logger.debug(f"Validating year: {year}")
    if len(year) != 4:
        logger.error(f"Invalid year format: {year}. Please provide a valid 4-digit year.")
        return False
    logger.debug(f"Year validation successful")
    return True


def get_gender_label(sex: str) -> str:
    """ Returns the gender label based on the provided sex. """

    female_terms = ["female", "women", "woman", "f", "w"]
    male_terms = ["male", "men", "man", "m"]

    logger.debug(f"Getting gender label for sex: {sex}")
    if sex.lower() in female_terms:
        return "women"
    elif sex.lower() in male_terms:
        return "men"
    else:
        logger.error(f"Invalid sex provided: {sex}. Defaulting to 'women'.")
        return "women"

def validate_arguments(args: list) -> tuple[list[str], str]:
    """ Validates the command line arguments for years and gender. """
    logger.debug(f"Validating command line arguments: {args}")
    years = []
    sex = SEX_FEMALE  # Default to women if not specified

    if len(sys.argv) <= 1:
        years.append(CURRENT_YEAR)
        logger.warning("No arguments were given. Defaulting to current year and women teams.")
        return years, sex        

    for arg in args[1:]:
        if is_valid_year(arg):
            years.append(arg)
        else:
            sex = get_gender_label(arg)

    if not years:
        logger.info("No valid years provided. Defaulting to current year.")
        years.append(CURRENT_YEAR)

    logger.debug(f"Validated years: {years}, sex: {sex}")
    return years, sex

