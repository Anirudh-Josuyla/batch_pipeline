import boto3
import os

def upload_to_s3(local_file_path, bucket_name, s3_file_name):
    """
    Upload a file to an S3 bucket.

    :param local_file_path: Path to the local file to upload
    :param bucket_name: Name of the S3 bucket
    :param s3_file_name: Name of the file in the S3 bucket
    """
    # Initialize a session using Amazon S3
    s3 = boto3.client('s3')

    try:
        # Upload the file
        s3.upload_file(local_file_path, bucket_name, s3_file_name)
        print(f"File '{local_file_path}' uploaded to '{bucket_name}/{s3_file_name}'")
    except Exception as e:
        print(f"Error uploading file: {e}")

def main():
    # Define the file you want to upload and the bucket name
    local_file_path = '/Users/anirudhjosuyla/Documents/batch_pipeline/data.csv'   # Replace with your local file path
    bucket_name = 'my-unique-bucketname'   # Replace with your S3 bucket name
    s3_file_name = 'data/file.csv'  # The name you want the file to have in S3

    # Check if the local file exists
    if os.path.exists(local_file_path):
        print(f"Uploading {local_file_path} to S3...")
        upload_to_s3(local_file_path, bucket_name, s3_file_name)
    else:
        print(f"The file '{local_file_path}' does not exist. Please check the path.")

if __name__ == "__main__":
    main()
