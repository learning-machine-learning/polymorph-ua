import pandas as pd
import sys
import pickle
import datetime
import pytz
from urllib.parse import unquote
from collections import defaultdict
from urllib.parse import unquote, urlparse
from pytz import timezone
import re

'''README

Call this script with python preprocess_script.py <input file as json> <output_file>
If output_file is blank, will automatically save to "input file + processed.h5"

ie: python preprocess_script.py data/combined_day1 data/day_1_processed.h5
'''

#gets hour from timestamp and 'geo_timezone'
def timestamp_to_local_hour(timezone, timestamp):
    hour = timestamp.split(':')[0][-2:]
    if pd.isna(timezone):
        return hour
    utc_time = datetime.datetime.utcnow()
    return pytz.utc.localize(utc_time, is_dst=None).astimezone(pytz.timezone(timezone)).hour

#replace NaNs in referer and url with blank strings
def replace_NaN_with_empty_string(val):
    if (isinstance(val, float) and math.isnan(val)) or val == None:
        return ""
    return val

#url referer keyword handling functions
def extract_parts(url):
    if url == None:
        url = ''
    o = urlparse(url)
    return o.netloc, o.path

def not_number(s):
    try:
        float(s)
        return False
    except ValueError:
        return True

def produce_keywords(path):
    MIN_LENGTH = 3
    BANNED_WORDS = ["html"]
    words = re.findall("[\w]+", path)
    filtered = [word for word in words if len(word) >= MIN_LENGTH and \
                word not in BANNED_WORDS and not_number(word)]
    return filtered

def append_keyword_cols(df):
    domains = {"url_domain": [], "ref_domain": []}
    keywords = {"url_keywords": [], "ref_keywords": [], "keywords": []}
    
    for url in df["url"]:
        domain, path = extract_parts(url)
        words = produce_keywords(path)
        domains["url_domain"].append(domain)
        keywords["url_keywords"].append(words)
    for ref in df["referer"]:
        url = unquote(ref)
        domain, path = extract_parts(url)
        words = produce_keywords(path)
        domains["ref_domain"].append(domain)
        keywords["ref_keywords"].append(words)
    
    df['url_domain'] = domains['url_domain']
    df['red_domain'] = domains['ref_domain']
    for i, j in zip(keywords['url_keywords'], keywords['ref_keywords']):
        keywords['keywords'].append(i+j)
    df['keywords'] = keywords['keywords']

file_path = sys.argv[1]
save_path = sys.argv[2]

if save_path == None or save_path == "":
    save_path = file_path + "processed.h5"

with open('data/columns_keep.pkl', 'rb') as f:
    columns_keep = pickle.load(f)

print(file_path)

df = pd.concat(pd.read_json(file_path, lines=True, chunksize=100000))

#Drop all columns that aren't in the final column list
df = df.drop([c for c in df.columns if c not in columns_keep], axis=1)

#Drop all rows with NaN values not in referer or url
df = df.dropna(subset=[c for c in df.columns if c not in ["referer", "url"]])

#convert all timestamps to local hours, while changing all NaNs to empty strings
for c in df.columns:
    if c.endswith('timestamp'):
        df[c] = [timestamp_to_local_hour(timezone, timestamp) for timezone, timestamp in zip(df['geo_timezone'].values,df[c].values)]
        df_pos[c] = [timestamp_to_local_hour(timezone, timestamp) for timezone, timestamp in zip(df_pos['geo_timezone'].values,df_pos[c].values)]
    if c in ["referer", "url"]:
        df[c] = df[c].apply(replace_NaN_with_empty_string)
        df_pos[c] = df_pos[c].apply(replace_NaN_with_empty_string)

append_keyword_cols(df)

#Open our hdf files
df_store = pd.HDFStore(save_path)

#Save our dataframes as hdf5
df_store['df'] = df

#Close our hdf files
df_store.close()
