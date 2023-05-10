import boto3
import click

@click.command()
@click.argument('bucket_name')
@click.argument('image_name')
def detect_text_in_s3(bucket_name, image_name):
    # Set up the client
    client = boto3.client('rekognition')

    # Call the detect_text method
    response = client.detect_text(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': image_name
            }
        }
    )

    # Print the detected text
    for text in response['TextDetections']:
        if text['Type'] == 'LINE':
            print(text['DetectedText'])

if __name__ == '__main__':
    detect_text_in_s3()
