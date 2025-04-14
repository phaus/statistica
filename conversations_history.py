import requests as rq
import pandas as pd
import os
import pprint

import csv

with open('users.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    user_dict = {row['USER_ID']:row['USER'] for row in reader}
    print(user_dict)

msg_url = 'https://slack.com/api/conversations.history'
token = os.environ['SLACK_TOKEN']
msg_params = {
    'limit': 1000,
    'channel': os.environ['SLACK_CHANNEL_ID'],
}
msg_headers = {'Authorization': 'Bearer ' + token, 'content-type': 'application/x-www-form-urlencoded'}

msg_res = rq.get(url=msg_url, headers=msg_headers, params=msg_params)

# print json to screen with human-friendly formatting
pprint.pprint(msg_res.json(), compact=True)

msg = [i['ts'] for i in msg_res.json()['messages']]
