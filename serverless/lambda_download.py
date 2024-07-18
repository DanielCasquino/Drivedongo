import boto3
import json

s3 = boto3.client('s3')
bucket_name = 'bucket-drive-main'

def lambda_handler(event, context):
    user_id = event['user_id']
    file_name = event['file_name']

    try:
        s3.head_object(
            Bucket=bucket_name,
            Key=f"{user_id}/{file_name}"
        )
        
        pre_signed_url = s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': f"{user_id}/{file_name}"
            },
            ExpiresIn=1800 # La URL expirará en 30 minutos
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'file_name': file_name,
                'download_url': pre_signed_url
            })
        }
    except s3.exceptions.NoSuchKey:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'File not found'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
