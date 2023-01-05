import json
from testing_json_file import lambda_handler as testing_json
from lambda1 import lambda_handler as lambda1
from lambda2 import lambda_handler as lambda2


def lambda_handler(event, context):
    # TODO implement
    if event['input_trigger'] == "testing_json":
        return testing_json(event, context)
    if event['input_trigger'] == "lambda1":
        return lambda1(event, context)
    if event['input_trigger'] == "lambda2":
        return lambda2(event, context)

