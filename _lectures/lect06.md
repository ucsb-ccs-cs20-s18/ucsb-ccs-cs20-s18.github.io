---
num: "Lecture 6"
desc: "Working with JSON files"
ready: false
date: 2017-04-19 12:30:00.00-7:00
---

# Sources of JSON files

* Earthquake data:  <https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php>
* Corgis Datasets: <https://think.cs.vt.edu/corgis/json/>
* Reddit: add ".json" to almost any url.  
    * For example, instead of <https://www.reddit.com/r/UCSantaBarbara/>, use <https://www.reddit.com/r/UCSantaBarbara.json>


# How to read a JSON file into a Python program

# Quick overview (more detail later in file)

## Read json  from file into dict

Code is in [readJson.py](readJson.py/)

Adapted from: <https://stackoverflow.com/questions/20199126/reading-json-from-a-file>

Assuming [`data_in.json`](data_in.json/) is a file containing:

```json
{
  "one":"uno",
  "two":"dos"
}
```

```python

import json

with open('data_in.json') as json_data:
    d = json.load(json_data)
    print(d)
```

## Write json from dict to file

Adapted from: <https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file>

This writes to a file called [`data_out.json`](data_out.json/).

Code is in [writeJson.py](writeJson.py/)

```
import json

data = {"one":"uno","two":"dos"}

print(data)

with open('data_out.json', 'w') as outfile:
    json.dump(data, outfile)

``` 
