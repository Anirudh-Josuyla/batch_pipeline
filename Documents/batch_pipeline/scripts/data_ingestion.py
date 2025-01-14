# Import necessary libraries
import boto3  # AWS SDK to interact with AWS services like S3
import json  # Used to convert Python objects into JSON format
from datetime import datetime  # To get current timestamp for the data

# Function to upload data to AWS S3
def upload_to_s3(data, bucket_name, object_name):
    """
    This function uploads the given data to the specified S3 bucket and object name.
    Arguments:
    - data: Data to upload (in Python dictionary format).
    - bucket_name: The name of the S3 bucket to upload to.
    - object_name: The S3 object key (path) where the data will be stored.
    """
    # Create an S3 client
    s3 = boto3.client('s3')

    # Upload the data to S3, converting it to JSON format using json.dumps()
    s3.put_object(Body=json.dumps(data), Bucket=bucket_name, Key=object_name)

    # Print a confirmation message when data is successfully uploaded
    print(f"Data uploaded to {bucket_name}/{object_name}")

# Function to simulate data ingestion
def ingest_data():
    """
    This function simulates the process of pulling data from an external source.
    It generates mock data and uploads it to an S3 bucket.
    """
    # Simulate data to be ingested (replace with actual data collection logic)
    data = {
        'timestamp': datetime.now().isoformat(),  # Current timestamp
        'event': 'user_posted',  # Simulating a user event
        'user': 'john_doe',  # Example user
        'content': 'This is a mock post!'  # Example content of the post
    }

    # S3 bucket where data will be stored (replace with your actual bucket name)
    bucket_name = 'my-s3-bucket-name'

    # Define a unique object name for each data file by using the current timestamp
    object_name = f"data/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"

    # Call the function to upload the data to S3
    upload_to_s3(data, bucket_name, object_name)

# Main entry point of the script
if __name__ == "__main__":
    # Call the function to ingest data
    ingest_data()
