from lambda_decorators import json_http_resp, load_json_body


@json_http_resp
@load_json_body
def echo(event, context):
    body = {
        "message": "Hello, test from users app handler!",
        "input": event,
    }
    return {"message": body}
