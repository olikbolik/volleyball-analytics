import os
import pandas as pd
from pathlib import Path

from constants import BASE_VNL_URL, YEAR, STATISTICS, SEX, DATA_DIR, RAW_DATA_FILE_EXTENSION

#url = 'https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/teams/women/'


if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

for metric in STATISTICS:
    metric_url = f"{BASE_VNL_URL}/{YEAR}/statistics/{SEX}/{metric}/?"
    tables = pd.read_html(metric_url)

    try:
        print(f"Tables found for {metric}: {len(tables)}")
        df = tables[0]
        # print(f"DataFrame for {metric}:")
        # print(df)
    except HTTPError as e:
        print(f"Invalid url for {metric}: {e}")  
    except ImportError(msg) as e:
        print(f"No tables found for {metric}: {e}")
    else:
        # Save the DataFrame to a CSV file
        raw_data_file = DATA_DIR/f"{metric}{RAW_DATA_FILE_EXTENSION}"
        df.to_csv(raw_data_file, index=False)
        print(f"{metric} processed successfully.")
    finally:
        print(f"Finished processing {metric}.\n")
print("end")
