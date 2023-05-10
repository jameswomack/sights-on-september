import boto3
import click
import os

@click.command()
@click.argument('bucket_name')
@click.argument('image_name')
def detect_logo_in_s3(bucket_name, image_name):
    import boto3

    # Set up the client
    client = boto3.client('rekognition')

    # Specify the S3 bucket and image name for the image that contains your logo
    logo_bucket_name = bucket_name
    logo_image_name = 'logo_bowman-chrome.png'

    # Call the detect_labels method on the image with the logo
    logo_response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': logo_bucket_name,
                'Name': logo_image_name
            }
        }
    )

    # Extract the name of the logo from the response
    logo_name = logo_response['Labels'][0]['Name']

    # Call the detect_custom_labels method
    custom_logo_response = client.detect_custom_labels(
        Image={
            'S3Object': {
                'Bucket': logo_bucket_name,
                'Name': logo_image_name
            }
        },
        ProjectVersionArn=os.environ.get('AWS_REKOGNITION_ARN'),
    )

    # Print the detected custom labels
    for label in custom_logo_response['CustomLabels']:
        print(label['Name'], label['Confidence'])

    # Call the detect_labels method on the image to check for the logo
    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': image_name
            }
        }
    )

    # Check if the logo is present in the image
    for label in response['Labels']:
        if label['Name'] == logo_name:
            print(f'{logo_name} is present in the image with confidence {label["Confidence"]:.2f}%')
        else:
          print(f'{logo_name} is not present in the image with confidence {label["Confidence"]:.2f}%')


if __name__ == '__main__':
    detect_logo_in_s3()
