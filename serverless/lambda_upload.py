import boto3
import json
import base64

s3 = boto3.client('s3')
bucket_name = 'bucket-drive-main'
sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/977155084989/drive-queue' # Pongan las de ustedes para que funcione

def lambda_handler(event, context):
    user_id = event['user_id']
    file_name = event['file_name']
    file_content = event['file_content']

    try:
        base64_content = file_content.split(',')[1]
        decoded_content = base64.b64decode(base64_content)

        s3.put_object(
            Bucket=bucket_name,
            Key=f"{user_id}/{file_name}",
            Body=decoded_content,
            ACL='public-read'
        )

        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps({'user_id': user_id, 'file_name': file_name})
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'Errors': str(e)})
        }
