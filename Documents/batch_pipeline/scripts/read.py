import boto3
import pandas as pd
from io import StringIO

def read_from_s3(bucket_name, s3_file_name):
    """
    Read a CSV file from S3 and load it into a pandas DataFrame.
    :param bucket_name: Name of the S3 bucket
    :param s3_file_name: S3 file name (path inside the bucket)
    :return: pandas DataFrame containing the CSV data
    """
    s3 = boto3.client('s3')

    try:
        # Download the file from S3
        obj = s3.get_object(Bucket=bucket_name, Key=s3_file_name)
        body = obj['Body'].read().decode('utf-8')  # Read the content
        df = pd.read_csv(StringIO(body))  # Load the data into pandas DataFrame
        print("File loaded successfully!")
        return df
    except Exception as e:
        print(f"Error reading file from S3: {e}")
        return None

# Replace with your bucket and file name
bucket_name = 'my-unique-bucketname'  # Your S3 bucket name
s3_file_name = 'data/file.csv'  # The file path in your S3 bucket

# Read the file and process it
data = read_from_s3(bucket_name, s3_file_name)

# If data is loaded successfully, perform basic analysis
if data is not None:
    print("Data preview:")
    print(data.head())  # Display the first few rows of the data
