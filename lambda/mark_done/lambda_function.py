import boto3
import json

dynamodb = boto3.resource("dynamodb")

def lambda_handler(event, context):
    table = dynamodb.Table("myTable")
    table.update_item(
        Key={"id": event["id"]},
        UpdateExpression="SET done = :val",
        ExpressionAttributeValues={":val": True}
    )

    return {
        "statusCode": 200,
        "body": json.dumps("Todo marked as done")
    }
