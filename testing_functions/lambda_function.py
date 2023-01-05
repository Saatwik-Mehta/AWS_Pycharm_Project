"""testing lambda function"""
import json


def lambda_handler(event, context):
    return dict(status=200, message="OK")
