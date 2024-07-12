import boto3
import json

lambda_client = boto3.client('lambda')  

def lambda_handler(event, context):
    token = event['headers']['Authorization']
    payload_string = '{ "token": "' + token +  '" }'
    invoke_response = lambda_client.invoke(FunctionName="lambda_auth",
                                           InvocationType='RequestResponse',
                                           Payload = payload_string)
    response = json.loads(invoke_response['Payload'].read())
    print(response)
    if response['statusCode'] == 403:
        return {
            'statusCode' : 403,
            'status' : 'Forbidden'
        }

    message = {
        'message': 'User auth works :)',
        }
    return {
        'statusCode': 200,
        'response': message
    }
