# import boto3
# import json

# lambda_client = boto3.client('lambda')
# bucket_name = 'bucket-drive-main'

# def lambda_handler(event, context):
#     token = event['headers']['Authorization']
#     payload_string = '{ "token": "' + token +  '" }'
#     invoke_response = lambda_client.invoke(FunctionName="lambda_auth",
#                                            InvocationType='RequestResponse',
#                                            Payload = payload_string)
#     response = json.loads(invoke_response['Payload'].read())
#     print(response)
#     if response['statusCode'] == 403:
#         return {
#             'statusCode' : 403,
#             'status' : 'Forbidden'
#         }
#     user_id = response['body'] # File is uploaded to folder with this name
#     # The bucket itself is named bucket-drive-main, but each user has a folder named after their used_id (email)
#     # We need to upload files to the folder, not the drive
#     # Read this pls

#     # Now we send the folder name, file, and file metadata to our SNS, so it can:
#     # - Call lambda that uploads the file to the corresponding folder
#     # - Cal another lambda that creates the metadata entry inside the Dyn table
#     # (DONT FORGET TO USE USER_ID AS PART AND FILE_ID AS SORT)
#     # Else you die

#     # When the file upload is finished, send email to user (dynamodb streams, look them up)
#     # Deletion would be handled similarly, except file is deleted together with metadata entry
#     # (using file_id as sorting key and user_id as partition key)

#     message = {
#         'message': 'File upload works for ' + user_id,
#         }
#     return {
#         'statusCode': 200,
#         'response': message
#     }


import boto3
import json
import base64

lambda_client = boto3.client('lambda')
sns_client = boto3.client('sns')
s3_client = boto3.client('s3')
bucket_name = 'bucket-drive-main'

def upload_file_to_s3(bucket_name, folder_name, file_content, file_name):
    try:
        s3_client.put_object(Bucket=bucket_name, Key=f"{folder_name}/{file_name}", Body=base64.b64decode(file_content))
        return True
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False

def lambda_handler(event, context):
    token = event['headers']['Authorization']
    payload_string = json.dumps({ "token": token })
    invoke_response = lambda_client.invoke(
        FunctionName="lambda_auth",
        InvocationType='RequestResponse',
        Payload=payload_string
    )
    response = json.loads(invoke_response['Payload'].read())
    print(response)
    if response['statusCode'] == 403:
        return {
            'statusCode' : 403,
            'status' : 'Forbidden'
        }

    user_id = response['body']
    folder_name = user_id
    file_content = event['body']['file_content']
    file_name = event['body']['file_name']
    file_id = event['body']['file_id']
    metadata = event['body']['metadata']

    if upload_file_to_s3(bucket_name, folder_name, file_content, file_name):
        sns_message = {
            'user_id': user_id,
            'file_id': file_id,
            'folder_name': folder_name,
            'file_name': file_name,
            'metadata': metadata
        }
        sns_client.publish(
            TopicArn='arn:aws:sns:your-sns-topic-arn',
            Message=json.dumps(sns_message)
        )
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'File uploaded successfully',
                'user_id': user_id
            })
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'File upload failed'
            })
        }
