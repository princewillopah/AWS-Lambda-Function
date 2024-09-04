import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb', region_name='eu-north-1') # Initialize a DynamoDB resource object for the specified region

    table = dynamodb.Table('studentData')  # Select the DynamoDB table named 'studentData'

    # Scan the table to retrieve all items
    response = table.scan()
    data = response['Items']

    # If there are more items to scan, continue scanning until all items are retrieved
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    # Return the retrieved data
    return data
