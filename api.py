import tomllib

import requests

try:
    with open("conf/config.toml", "rb") as f:
        config = tomllib.load(f)
except FileNotFoundError:
    print("No config found! Please setup your config.toml from the template!")
    exit(1)

API_KEY = config["API-CONFIG"]["api_key"]
API_TOKEN = config["API-CONFIG"]["api_token"]
API_URL = config["API-CONFIG"]["api_base_url"]

# Set your authentication credentials (API key or bearer token)
HEADERS = {
    "accept": "application/json;charset=UTF-8",
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json;charset=UTF-8",
}


def get_domain_data(domain_name):
    url = f"{API_URL}/domains/{domain_name}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        domain_info = response.json()
        print(f"Domain data for {domain_name}:")
        print(domain_info)
    else:
        print(f"Error fetching domain data for {domain_name}. Status code: {response.status_code} error message:"
              f"{response.content}")


def get_zone_data(domain_name):
    url = f"{API_URL}/zones/{domain_name}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        domain_info = response.json()
        print(f"Zone data for {domain_name}:")
        print(domain_info)
    else:
        print(f"Error fetching domain data for {domain_name}. Status code: {response.status_code} error message:"
              f"{response.content}")


def add_zone_data(domain_name: str, record_type: str, key: str, value: str, ttl: int = 300, change_id: str = "",
                  comments: str = "Created via Niklas Python API Script"):
    url = f"{API_URL}/zones/edits"
    body = {
        "zoneName": domain_name,
        "edits": [
            {
              "recordType": record_type,
              "action": "ADD",
              "newKey": key,
              "newValue": value,
              "newTtl": ttl,
              "changeId": change_id,
              "comments": comments
            }
        ]
    }
    response = requests.post(url, headers=HEADERS, json=body)
    if response.status_code == 201:
        domain_info = response.json()
        print(f"Zone data for {domain_name}:")
        print(domain_info)
    else:
        print(f"Error adding record for {key}.{domain_name} with status code: {response.status_code} and error message:"
              f"{response.content}")


def remove_zone_data(domain_name: str, record_type: str, key: str, value: str, ttl: int = 300, change_id: str = "",
                  comments: str = "Created via Niklas Python API Script"):
    url = f"{API_URL}/zones/edits"
    body = {
        "zoneName": domain_name,
        "edits": [
            {
              "recordType": record_type,
              "action": "PURGE",
              "currentKey": key,
              "currentValue": value
            }
        ]
    }
    response = requests.post(url, headers=HEADERS, json=body)
    if response.status_code == 201:
        domain_info = response.json()
        print(f"Zone data for {domain_name}:")
        print(domain_info)
    else:
        print(f"Error adding record for {key}.{domain_name} with status code: {response.status_code} and error message:"
              f"{response.json()}")

