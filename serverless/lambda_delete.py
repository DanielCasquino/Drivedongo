import boto3

s3 = boto3.client('s3')
bucket_name = 'bucket-drive-main'

def lambda_handler(event, context):
    user_id = event['user_id']
    file_name = event['file_name']

    try:
        response = s3.delete_object(
            Bucket=bucket_name,
            Key=f"{user_id}/{file_name}"
        )

        return {
            'statusCode': 200,
            'body': 'File deleted successfully',
            'payload': {
                'user_id': user_id,
                'file_name': file_name
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': 'An error occurred',
            'payload': {
                'Errors': str(e)
            }
        }
