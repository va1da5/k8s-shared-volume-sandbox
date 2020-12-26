import json
import os

with open("config.json") as config_file:
    config_json = config_file.read()

SETTINGS = json.loads(config_json)

HOSTNAME = os.getenv("HOSTNAME")