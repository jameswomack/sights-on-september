import os
import boto3
import click

@click.command()
@click.argument('bucket_name')
@click.argument('file_path')
def upload_file_to_s3(bucket_name, file_path):
    # Set up the client
    s3 = boto3.resource('s3')

    file_name = os.path.basename(file_path)

    # Upload the file
    s3.meta.client.upload_file(file_path, bucket_name, file_name)

    # Print success message
    print(f'File uploaded successfully to s3://{bucket_name}/{file_name}')

if __name__ == '__main__':
    upload_file_to_s3()