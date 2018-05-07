import gzip
import json

import boto3
import os

s3 = boto3.resource('s3')
s3client = boto3.client('s3')

as_bucket_name = 'codebase-pm-ua-filtered'
cb_bucket_name = 'codebase-pm-ua-filtered'

TEMP_INPUT_FILE_NAME = 'temp_in.gz'
TEMP_OUTPUT_FILE_NAME = 'temp_out.gz'

# Total Files: 15,360
# START_INDEX = 0
# STOP_INDEX = 2000

CONTINUATION_TOKEN = None

try:
    os.remove(TEMP_INPUT_FILE_NAME)
except OSError:
    pass
try:
    os.remove(TEMP_OUTPUT_FILE_NAME)
except OSError:
    pass

as_objects = s3client.list_objects_v2(Bucket=as_bucket_name)

as_bucket = s3.Bucket(name=as_bucket_name)
cb_bucket = s3.Bucket(name=cb_bucket_name)

# file_keys = [item['Key'] for item in as_objects['Contents'] if 'part' in item['Key']][START_INDEX:STOP_INDEX]

file_keys = []
combined_keys = []
for d in range(4, 5):
    for h in range(0, 24):
        file_keys.append('merged_logs/%02d/%02d/combined_positives.gz' % (d, h ))
    combined_keys.append('merged_logs/%02d/combined_day_positives.gz' % (d))

print(combined_keys)
# file_keys = file_keys[START_INDEX:STOP_INDEX]

# keys_to_pop = [
#     # Duplicate Keys
#     "r_timestamp", "pub_network_id", "geo_country_code2", "site_id", "session_id", "geo_continent_code", "zone_id",
#     # Unique Keys
#     "bid_req_cnt", "bid_resp_cnt", "bid_price", "campaign_id"
# ]

zip_count = 0
combined_key_count = 0
for file_key in file_keys:
    zip_count += 1
    print(file_key)
    try:
        as_bucket.download_file(Key=file_key, Filename=TEMP_INPUT_FILE_NAME)
        with gzip.open(TEMP_INPUT_FILE_NAME, 'rt') as f:
            lines = f.readlines()
            f.close()

        if zip_count == 1:
            filtered_output = gzip.open(TEMP_OUTPUT_FILE_NAME, 'wt')

        index = 0
        while index < len(lines):
            line_dict = json.loads(lines[index])
            line = json.dumps(line_dict)
            filtered_output.write(line + "\n")
            index += 1

    except:
        print("failed to add file of " + str(file_key) + " to combined gzip! Sad!")
    if zip_count >= 24:
        zip_count = 0
        filtered_output.close()
        cb_bucket.upload_file(Filename=TEMP_OUTPUT_FILE_NAME, Key=combined_keys[combined_key_count])
        combined_key_count += 1

