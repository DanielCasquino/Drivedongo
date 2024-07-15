import uuid
import boto3
import hashlib
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('t_driveUsers')
tokenTable = dynamodb.Table('t_driveTokens')

def lambda_handler(event, context):
    user_id = event.get('user_id')
    password = event.get('password')
    
    if not user_id or not password:
        return {
            "statusCode": 400,
            "body": 'Email and password are required'
        }
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    response = table.get_item(
        Key={
            'user_id': user_id
        }
    )
    if 'Item' not in response:
        return {
            'statusCode': 404,
            'body': 'User does not exist'
        }
    else:
        hashed_password_bd = response['Item']['password']
        if hashed_password == hashed_password_bd:
            token = str(uuid.uuid4())
            exp = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=60)
            tokenRegister = {
                'token': token,
                'user_id': user_id,
                'expires': exp.strftime('%Y-%m-%d %H:%M:%S')
            }
            dynamodbResponse = tokenTable.put_item(Item = tokenRegister)
        else:
            return {
                'statusCode': 403,
                'body': 'Incorrect credentials'
            }
    return {
        'statusCode': 200,
        'token': token
    }