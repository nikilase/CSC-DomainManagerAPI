import tomllib

try:
	with open("conf/config.toml", "rb") as f:
		config = tomllib.load(f)
		config_exists = True
except FileNotFoundError:
	print("No config found! Please setup your config.toml from the template!")
	# ToDo: Here we could then ask if the user wants to put in the information and we write it to a config file
	# 	Or if the user wants to supply the file themselves
	exit(1)

API_KEY = config["API-CONFIG"]["api_key"]
API_TOKEN = config["API-CONFIG"]["api_token"]
API_URL = config["API-CONFIG"]["api_base_url"]