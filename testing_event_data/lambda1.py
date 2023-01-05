from random import choice
def lambda_handler(event, context):
    print(event)
    # Do something with input received
    input_data =event["input"]
    statuses=["PROCESSED", "FAILED", "QUEUED"]
    input_data.update(status=choice(statuses))
    return input_data