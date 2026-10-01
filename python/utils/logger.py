import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File handler - keeps important information
file_handler = logging.FileHandler("vb_analysis.log")
file_handler.setLevel(logging.INFO)

# Console handler - detailed information 
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

