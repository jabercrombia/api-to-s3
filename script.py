import os
import boto3
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get values from .env
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_FILE_PATH = os.getenv("S3_FILE_PATH")

# Fetch weather data
CITY = "London"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# Convert JSON to DataFrame
df = pd.json_normalize(data)

# Save to CSV
csv_path = "weather.csv"
df.to_csv(csv_path, index=False)
print(f"✅ CSV saved: {csv_path}")

# Upload to S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

try:
    s3.upload_file(csv_path, S3_BUCKET_NAME, S3_FILE_PATH)
    print(f"✅ Successfully uploaded to S3: s3://{S3_BUCKET_NAME}/{S3_FILE_PATH}")
except Exception as e:
    print(f"❌ Failed to upload file: {e}")
