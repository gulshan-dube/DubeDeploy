import json

def lambda_handler(event, context):
    query_params = event.get("queryStringParameters") or {}
    name = query_params.get("name", "world")

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Hello, {name}!"})
    }
