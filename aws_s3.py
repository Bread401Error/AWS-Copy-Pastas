import boto3
import botocore

# download file from s3
def download_s3_file(bucket_name, obj_name, file_name):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, obj_name, file_name)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        return False
    return True

# upload file to s3
def upload_s3_file(file_name, bucket_name, obj_name):
    s3 = boto3.resource('s3')
    try:
        s3.meta.client.upload_file(file_name, bucket_name, obj_name)
    except botocore.exceptions.ClientError as e:
        return False
    return True
