import serverless_sdk
sdk = serverless_sdk.SDK(
    org_id='dennytarn',
    application_name='aws-course-app',
    app_uid='3wZqjYMxDQNYXdDM41',
    org_uid='d8fc46bc-85b9-44ff-8211-dfbba356ecb5',
    deployment_uid='7e9b3886-24e9-4771-91c8-7ecca83b6f0a',
    service_name='aws-course-app',
    should_log_meta=True,
    should_compress_logs=True,
    disable_aws_spans=False,
    disable_http_spans=False,
    stage_name='dev',
    plugin_version='5.5.1',
    disable_frameworks_instrumentation=False,
    serverless_platform_stage='prod'
)
handler_wrapper_kwargs = {'function_name': 'aws-course-app-dev-hello', 'timeout': 6}
try:
    user_handler = serverless_sdk.get_user_handler('apps/users/handlers.echo')
    handler = sdk.handler(user_handler, **handler_wrapper_kwargs)
except Exception as error:
    e = error
    def error_handler(event, context):
        raise e
    handler = sdk.handler(error_handler, **handler_wrapper_kwargs)
