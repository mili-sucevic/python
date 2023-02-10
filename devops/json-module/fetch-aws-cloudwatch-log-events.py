import boto3
import json

def fetch_cloudwatch_log_events(log_group_name, log_stream_name, start_time, end_time):
    cloudwatch_logs = boto3.client("logs")
    response = cloudwatch_logs.filter_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        startTime=start_time,
        endTime=end_time
    )
    
    events = response["events"]
    for event in events:
        print(event["message"])

fetch_cloudwatch_log_events("my-log-group", "my-log-stream", 1605657600, 1605657660)
