import os


def directory_exists(directory_path):
    logger.debug(f"Checking if directory exists at {directory_path}")
    return os.path.exists(directory_path)

def create_directory(directory_path):
    logger.debug(f"Creating directory at {directory_path}")  
    os.makedirs(directory_path)
    logger.info(f"Directory created at {directory_path}")
