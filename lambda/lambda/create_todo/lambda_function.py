import json
import boto3

dynamodb = boto3.resource("dynamodb")

def lambda_handler(event, context):
    table = dynamodb.Table("myTable")
    table.put_item(Item=event)

    return {
        "statusCode": 200,
        "body": json.dumps("Todo created successfully")
    }
