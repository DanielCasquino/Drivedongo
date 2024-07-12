import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('t_driveTokens')

def lambda_handler(event, context):
    token = event['token']

    response = table.get_item(
        Key={
            'token': token
        }
    )
    if 'Item' not in response:
        return {
            'statusCode': 403,
            'body': 'Token does not exist'
        }
    else:
        expires = response['Item']['expires']
        now = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M:%S')
        if now > expires:
            return {
                'statusCode': 403,
                'body': 'Token expired'
            }
    
    # Salida (json)
    return {
        'statusCode': 200,
        'body': 'Token is valid'
    }