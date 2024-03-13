import tomllib

import click

config_exists = False

try:
    with open("app/conf/config.toml", "rb") as f:
        config = tomllib.load(f)
        config_exists = True
except FileNotFoundError:
    print("No config found! Please setup your config.toml from the template!")
    if not click.confirm("Do you want to continue?", default=True):
        exit(1)

if config_exists:
    API_KEY = config["API-CONFIG"]["api_key"]
    API_TOKEN = config["API-CONFIG"]["api_token"]
    API_URL = config["API-CONFIG"]["api_base_url"]
else:
    API_KEY = input("Enter your API Key:")
    API_TOKEN = input("Enter your API Token:")
    API_URL = input("Enter your API Base URL:")
