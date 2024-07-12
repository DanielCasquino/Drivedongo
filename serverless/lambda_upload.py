import boto3
import json

lambda_client = boto3.client('lambda')
bucket_name = 'bucket-drive-main'

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
    user_id = response['body'] # File is uploaded to folder with this name
    # The bucket itself is named bucket-drive-main, but each user has a folder named after their used_id (email)
    # We need to upload files to the folder, not the drive
    # Read this pls

    # Now we send the folder name, file, and file metadata to our SNS, so it can:
    # - Call lambda that uploads the file to the corresponding folder
    # - Cal another lambda that creates the metadata entry inside the Dyn table
    # (DONT FORGET TO USE USER_ID AS PART AND FILE_ID AS SORT)
    # Else you die

    # When the file upload is finished, send email to user (dynamodb streams, look them up)
    # Deletion would be handled similarly, except file is deleted together with metadata entry
    # (using file_id as sorting key and user_id as partition key)

    message = {
        'message': 'File upload works for ' + user_id,
        }
    return {
        'statusCode': 200,
        'response': message
    }
