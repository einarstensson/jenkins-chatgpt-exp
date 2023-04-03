import boto3
import os

# Set up the S3 client
session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)
s3 = session.client('s3')

# Set the bucket name
bucket_name = os.environ['EXP_BUCKET_NAME']

# List the contents of the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# Print the object keys
for item in response['Contents']:
    print(item['Key'])
