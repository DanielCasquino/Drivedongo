import boto3
import json
import base64

s3 = boto3.client('s3')
bucket_name = 'bucket-drive-main'

def lambda_handler(event, context):
    user_id = event['user_id']
    file_name = event['file_name']

    try:
        response = s3.get_object(
            Bucket=bucket_name,
            Key=f"{user_id}/{file_name}"
        )
        file_content = response['Body'].read()

        encoded_file_content = base64.b64encode(file_content).decode('utf-8')

        return {
            'statusCode': 200,
            'body': json.dumps({
                'file_name': file_name,
                'file_content': encoded_file_content
            }),
            'isBase64Encoded': True,
            'headers': {
                'Content-Disposition': f'attachment; filename={file_name}',
                'Content-Type': response['ContentType']
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
