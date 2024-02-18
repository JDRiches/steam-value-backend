# Some pytoh script to clean up the native response from steam web api
# Turns it into a more efficient dictionary

import json

with open('app_list.json', encoding='utf8') as f:
    raw_apps = json.load(f)

apps = {}
for entry in raw_apps['apps']:
    apps[entry['appid']] = entry['name']


with open('clean_app_list.json', 'w') as f:
    json.dump(apps,f)