import boto3
import click

@click.command()
@click.argument('bucket_name')
@click.argument('source_image_name')
@click.argument('target_image_name')
def compare_faces_in_s3(bucket_name, source_image_name, target_image_name):
    # Set up the client
    client = boto3.client('rekognition')

    # Compare the faces
    response = client.compare_faces(
        SourceImage={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': source_image_name
            }
        },
        TargetImage={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': target_image_name
            }
        },
        SimilarityThreshold=80.0  # Set the similarity threshold
    )

    # Print the results
    if len(response['FaceMatches']) > 0:
        similarity = response['FaceMatches'][0]['Similarity']
        print(f'The faces match with a similarity score of {similarity}%')
    else:
        print('The faces do not match')

if __name__ == '__main__':
    compare_faces_in_s3()
