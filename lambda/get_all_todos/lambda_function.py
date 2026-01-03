import boto3
import json
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource("dynamodb")

def lambda_handler(event, context):
    table = dynamodb.Table("myTable")
    response = table.scan(
        FilterExpression=Attr("done").eq(False)
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response.get("Items", []))
    }
