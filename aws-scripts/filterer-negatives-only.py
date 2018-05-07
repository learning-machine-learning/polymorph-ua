import gzip
import json

import boto3
import os
import random

s3 = boto3.resource('s3')
s3client = boto3.client('s3')

as_bucket_name = 'adsnative-sigmoid'
cb_bucket_name = 'codebase-pm-ua-filtered'

TEMP_INPUT_FILE_NAME = 'temp_in.gz'
TEMP_OUTPUT_FILE_NAME = 'temp_out.gz'

# Total Files: 15,360
START_INDEX = 0
STOP_INDEX = 3000

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
for d in range(1, 8):
    for h in range(0, 24):
        for n in range(0, 128):
            file_keys.append('merged_logs/%02d/%02d/part-00%03d.gz' % (d, h, n))

file_keys = file_keys[START_INDEX:STOP_INDEX]

# keys_to_pop = [
#     # Duplicate Keys
#     "r_timestamp", "pub_network_id", "geo_country_code2", "site_id", "session_id", "geo_continent_code", "zone_id",
#     # Unique Keys
#     "bid_req_cnt", "bid_resp_cnt", "bid_price", "campaign_id"
# ]

for file_key in file_keys:
    print(file_key)
    try:
        as_bucket.download_file(Key=file_key, Filename=TEMP_INPUT_FILE_NAME)

        with gzip.open(TEMP_INPUT_FILE_NAME, 'rt') as f:
            lines = f.readlines()
            f.close()
        filtered_output = gzip.open(TEMP_OUTPUT_FILE_NAME, 'wt')

        index = 0
        while index < len(lines):
            line_dict = json.loads(lines[index])
            try:
                index += 1
                if "c_cnt" in line_dict and line_dict["c_cnt"] == 0:
                    if random.randint(1,500) == 1:
                        line = json.dumps(line_dict)
                        filtered_output.write(line + "\n")
            except:
                continue

        filtered_output.close()

        cb_bucket.upload_file(Filename=TEMP_OUTPUT_FILE_NAME, Key=file_key[:-3] + "_negatives_pt2_percent.gz")
    except:
        print("filename of " + str(file_key) + " failed! Sad!")
