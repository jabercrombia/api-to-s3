import os
import boto3
import csv
from botocore.config import Config
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get value from .env
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_FILE_PATH = os.getenv("S3_FILE_PATH")

# Fetch weather data
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={OPENWEATHER_API_KEY}&units=imperial"

response = requests.get(URL)
data = response.json()

# Extract the forecast list
data_list = data["list"]

# Define CSV file name
city_name = data["city"]["name"]
city_name = city_name.lower()
csv_filename = f"weather_forecast_{city_name}.csv"

# Write to CSV
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(["Datetime", "Temperature", "Feels Like", "Min Temp", "Max Temp", "Pressure", "Humidity", "Weather Description"])
    
    # Write the data rows
    for entry in data_list:
        writer.writerow([
            entry["dt_txt"],
            entry["main"]["temp"],
            entry["main"]["feels_like"],
            entry["main"]["temp_min"],
            entry["main"]["temp_max"],
            entry["main"]["pressure"],
            entry["main"]["humidity"],
            entry["weather"][0]["description"]
        ])

print(f"Weather data has been exported to {csv_filename}")


# Upload to S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION,
    config=Config(signature_version='s3v4')
)

try:
    s3.upload_file(csv_filename, S3_BUCKET_NAME, S3_FILE_PATH)
    print(f"Successfully uploaded to S3: s3://{S3_BUCKET_NAME}/{S3_FILE_PATH}")
except Exception as e:
    print(f"❌ Failed to upload file: {e}")