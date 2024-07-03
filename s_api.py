import serverless_sdk
sdk = serverless_sdk.SDK(
    org_id='srinivas8919',
    application_name='aws-python-flask-api-project',
    app_uid='DQR8HXlY1gkBxDnjn0',
    org_uid='a93c8e2c-c2f1-429d-ab61-27f3eb30b429',
    deployment_uid='bd0f58e1-1d56-4e5d-bd6e-86001aff01de',
    service_name='aws-python-flask-api-project',
    should_log_meta=True,
    should_compress_logs=True,
    disable_aws_spans=False,
    disable_http_spans=False,
    stage_name='dev',
    plugin_version='7.0.3',
    disable_frameworks_instrumentation=False,
    serverless_platform_stage='prod'
)
handler_wrapper_kwargs = {'function_name': 'aws-python-flask-api-project-dev-api', 'timeout': 15}
try:
    user_handler = serverless_sdk.get_user_handler('wsgi_handler.handler')
    handler = sdk.handler(user_handler, **handler_wrapper_kwargs)
except Exception as error:
    e = error
    def error_handler(event, context):
        raise e
    handler = sdk.handler(error_handler, **handler_wrapper_kwargs)
