import requests
import json

URL = "http://127.0.0.1:8000/studentcreate/"

data = {
    'name' : 'Sonam',
    'roll' : 101,
    'city': 'Ranchi'
}
# to convert python data in json data
json_data = json.dumps(data)

# response stored in r
r = requests.post(url = URL, data = json_data)

# to extract data from r 
data = r.json()

print(data)