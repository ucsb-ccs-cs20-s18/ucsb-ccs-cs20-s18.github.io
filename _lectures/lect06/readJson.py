
import json

with open('data_in.json') as json_data:
    d = json.load(json_data)
    print(d)
