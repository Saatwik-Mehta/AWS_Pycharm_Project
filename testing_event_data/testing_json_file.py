import uuid
import json
import boto3
import tempfile
import logging
from botocore.exceptions import ClientError
import os

S3 = boto3.client('s3')



def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file

    try:
        response = S3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def create_array_pack(inputs):
    outer_list = []
    arr_range = 0
    while arr_range < len(inputs):
        outer_list.append(inputs[arr_range: arr_range + 32])
        arr_range += 32
    return outer_list


def lambda_handler(event, context):
    # write data into s3 and return the count of the data written
    bucket_name = event["bucket_name"]
    execution_id_arn = event["executionId"]  # Arn of execution id of sf
    execution_id = execution_id_arn[-36:]
    data_array = [{"event_id": str(uuid.uuid4()), "event_amount": 20000} for i in range(100)]
    # data_array=create_array_pack(data)

    with tempfile.TemporaryDirectory() as temp_dir:
        file = "input_for_map.json"
        filename = os.path.join(temp_dir, "input_for_map.json")
        with open(filename, "w+", newline="", encoding="utf-8") as jsonfile:
            json.dump(data_array, fp=jsonfile)
        upload_file(filename, "s3-event-data-bucket", object_name=f"{execution_id}{os.sep}{file}")
    return dict(data_array_count=len(data_array), bucket_name="s3-event-data-bucket",
                key_name=f"{execution_id}{os.sep}{file}", prefix=f"{execution_id}{os.sep}output")