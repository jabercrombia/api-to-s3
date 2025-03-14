# Weather Data ETL Pipeline

This project fetches weather data from the OpenWeather API, saves it as a CSV file locally, and then uploads it to an AWS S3 bucket.

## Prerequisites

### 1. Install Python and Pip
Ensure you have Python installed. If you don’t have `pip`:
```sh
python3 -m ensurepip --default-pip
python3 -m pip install --upgrade pip
```

### 2. Install Required Dependencies
```sh
pip install requests pandas boto3 python-dotenv
```

### 3. Configure AWS Credentials
Set up your AWS credentials for authentication:
```sh
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_key"
export AWS_DEFAULT_REGION="your_region"
```
Or configure them using AWS CLI:
```sh
aws configure
```

## Project Structure
```
api-to-s3/
│── .env                # Stores API key and AWS credentials
│── script.py           # Main ETL script
│── requirements.txt    # Python dependencies
│── README.md           # Documentation
```

## Setup Environment
Create and activate a virtual environment (recommended):
```sh
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

## OpenWeather API Setup
Create a `.env` file and add your OpenWeather API key:
```
OPENWEATHER_API_KEY=your_api_key
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region
S3_BUCKET_NAME=jabercrombia
S3_OBJECT_KEY=weatherapi/weather.csv
```

## Running the ETL Script
Execute the Python script to fetch weather data, save it locally, and upload it to S3:
```sh
python script.py
```

## Common Errors & Fixes

### 1. `ModuleNotFoundError: No module named 'requests'`
Ensure dependencies are installed:
```sh
pip install -r requirements.txt
```

### 2. `zsh: command not found: aws`
AWS CLI is not installed. Install it:
```sh
brew install awscli  # MacOS
sudo apt install awscli  # Ubuntu
```

### 3. `SignatureDoesNotMatch`
- Check AWS credentials: `aws configure`
- Ensure system time is synced:
```sh
sudo ntpdate -u time.apple.com  # Mac
w32tm /resync  # Windows
```

### 4. `AccessDenied: Not authorized to perform s3:GetBucketLocation`
Attach correct policies to your IAM user.

## Next Steps
- Set up an AWS Lambda function to automate uploads.
- Use Amazon Athena to query CSV data directly in S3.

---
**Author**: Your Name  
**Date**: March 2025  

