"""
A simple Lambda wrapped with Epsagon
"""
import os
import epsagon

EPSAGON_APP_NAME = (
    os.environ['EPSAGON_APP_NAME']
    if os.environ['EPSAGON_APP_NAME'] != ''
    else 'Default App'
)
epsagon.init(
    token=os.environ['EPSAGON_TOKEN'],
    app_name=EPSAGON_APP_NAME
)

@epsagon.lambda_wrapper
def handler(event, context):
    # Your code goes here!
    return 'Hello World!'

