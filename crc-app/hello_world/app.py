import json
import boto3

# import requests
# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('crc-views')
views = -1

def lambda_handler(event, context):
    
    response = table.get_item(
    Key={
        'ID': '1'
    })
    views = response['Item']['views']
    views += 1
    table.put_item(
       Item={
            'ID': '1',
            'views': views
    })
    return {
        "headers": {
            "Access-Control-Allow-Origin":  "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*"
        },
        "statusCode": 200,
        "body": json.dumps({
            "views": str(views)
        })
    }