from datetime import datetime
def lambda_handler(event, context):
    print(event)
    # Do something with input received
    input_data=event['input']['lambda1_result']['data']
    input_data.update(time=str(datetime.utcnow().time()))
    return input_data