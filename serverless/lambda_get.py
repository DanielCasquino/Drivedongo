import boto3
import base64

s3 = boto3.client('s3')
bucket_name = 'bucket-drive-main'

def lambda_handler(event, context):
    user_id = event['user_id']

    try:
        response = s3.list_objects_v2(
            Bucket=bucket_name,
            Prefix=f"{user_id}/"
        )

        files = []
        if 'Contents' in response:
            for obj in response['Contents']:
                file_info = {
                    'file_name': obj['Key'],
                    'upload_date': obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S'),
                    'file_type': obj['Key'].split('.')[-1]
                }

                if file_info['file_type'].lower() in ['jpg', 'jpeg', 'png', 'gif']:
                    image_response = s3.get_object(
                        Bucket=bucket_name,
                        Key=obj['Key']
                    )
                    file_info['image'] = base64.b64encode(image_response['Body'].read()).decode('utf-8')
                else:
                    file_info['image'] = None

                files.append(file_info)

        return {
            'statusCode': 200,
            'body': 'Files retrieved successfully',
            'payload': {
                'user_id': user_id,
                'files': files
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
