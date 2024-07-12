import json
import boto3
import hashlib
import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('t_driveUsers')
bucket_name = 'bucket-drive-main'

def lambda_handler(event, context):
    try:
        user_id = event.get('user_id')
        password = event.get('password')

        if user_id and password:
            # Check if the email already exists
            response = table.get_item(
                Key={'user_id': user_id}
            )
            if 'Item' in response:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'message': 'User with this email already exists'})
                }

            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            created_at = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M:%S')

            table.put_item(
                Item={
                    'user_id': user_id,
                    'password': hashed_password,
                    'created_at': created_at
                }
            )

            folder_key = f"{user_id}/"
            s3.put_object(Bucket=bucket_name, Key=folder_key) # Create a personal folder for new user

            message = {
                'message': 'User registered successfully',
                'user_id': user_id
                }
            return {
                'statusCode': 200,
                'body': message
            }
        else:
                message = {
                    'error': 'Invalid request body: missing user_id or password'
                }
                return {
                    'statusCode': 400,
                    'body': message
                }
    except Exception as e:
        print("Exception:", str(e))
        message = {
            'error': str(e)
        }        
        return {
            'statusCode': 500,
            'body': message
        }
