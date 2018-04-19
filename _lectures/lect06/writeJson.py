import json

data = {"one":"uno","two":"dos"}

print(data)

with open('data_out.json', 'w') as outfile:
    json.dump(data, outfile)


