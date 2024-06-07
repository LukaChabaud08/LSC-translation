import requests
import json
from dotenv import load_dotenv
import os
import sys
from datetime import datetime, timedelta
import time

load_dotenv()
key = os.getenv("METEOCAT_API_KEY")


def fetch_weather_predictions(output_directory: str):
    base_url = "https://api.meteo.cat/pronostic/v1"
    headers = {"Content-Type": "application/json", "X-Api-Key": key}

    today = datetime.today()
    date_list = [today + timedelta(days=x) for x in range(3)]

    for i, date in enumerate(date_list):
        year = date.year
        month = f"{date.month:02d}"  # Ensure two-digit month
        day = f"{date.day:02d}"  # Ensure two-digit day

        url = f"{base_url}/catalunya/{year}/{month}/{day}"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 400:
                print(response.json())
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            with open(
                os.path.join(output_directory, f"meteocat_{year}_{month}_{day}.json"),
                "w+",
            ) as fp:
                json.dump(data, fp)
            # print(f"Date: {year}-{month}-{day}, Data: {data}")

            # print(f"Sent request to {url}")
            # print(f"Stored response in {os.path.join(output_directory, f"meteocat_{i}.json")}")
            # print()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data for {year}-{month}-{day}: {e}")


if len(sys.argv) < 2:
    print("Missing output directory")
    sys.exit()
# Run the function
fetch_weather_predictions(sys.argv[1])
