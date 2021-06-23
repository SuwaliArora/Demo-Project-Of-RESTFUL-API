#third party application
import requests
import json

URL = "http://127.0.0.1:8000/studentdata/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    # to extract data from r 
    data = r.json()
    print(data)

get_data()

def post_data():
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

post_data()

def update_data():
    data = {
        'id': 2,
        'name' : 'ravish',
        'roll': 100,
        'city': 'goa'
    }
    # to convert python data in json data
    json_data = json.dumps(data)
    # response stored in r
    r = requests.put(url = URL, data = json_data)
    # to extract data from r 
    data = r.json()
    print(data)

update_data()

def delete_data():
    data = {
        'id': 6
    }
    # to convert python data in json data
    json_data = json.dumps(data)
    # response stored in r
    r = requests.delete(url = URL, data = json_data)
    # to extract data from r 
    data = r.json()
    print(data)

delete_data()
