import requests as rq
import pandas as pd
import os

channel_url = 'https://slack.com/api/conversations.list'
token = os.environ['SLACK_TOKEN']
channel_params = {
    'limit': 1000,
    'exclude_archived': True
}
channel_headers = {'Authorization': 'Bearer ' + token, 'content-type': 'application/x-www-form-urlencoded'}

channel_res = rq.get(url=channel_url, headers=channel_headers, params=channel_params)

channel_data = []
print(channel_res.json())
for i in channel_res.json()['channels']:
    channel_data.append({
        'id': i['id'],
        'name': i['name'],
        'created': i['created'],
        'members': i['num_members'],
        'is_group': i['is_group']
    })
    
channel_df = pd.DataFrame(channel_data).sort_values('members', ascending=False)
print(channel_df)
