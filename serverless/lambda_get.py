import boto3
import json
import base64
from PIL import Image
from io import BytesIO

s3 = boto3.client('s3')
bucket_name = 'bucket-drive-main'

def resize_image(image_data, scale_factor):
    image = Image.open(BytesIO(image_data))
    new_size = (image.width // scale_factor, image.height // scale_factor)
    resized_image = image.resize(new_size, Image.ANTIALIAS)
    buffer = BytesIO()
    resized_image.save(buffer, format=image.format)
    return buffer.getvalue()

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
                file_key = obj['Key']
                file_name = file_key[len(f"{user_id}/"):]
                file_info = {
                    'file_name': file_name,
                    'upload_date': obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S'),
                    'file_type': file_key.split('.')[-1],
                    'size': obj['Size']
                }

                if file_info['file_type'].lower() in ['jpg', 'jpeg', 'png', 'gif']:
                    image_response = s3.get_object(
                        Bucket=bucket_name,
                        Key=file_key
                    )
                    resized_image_data = resize_image(image_response['Body'].read(), 4)
                    file_info['image'] = base64.b64encode(resized_image_data).decode('utf-8')
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
