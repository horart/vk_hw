import json

with open("config.json") as f:
	config = json.load(f)


print("Hello world,", config["users"][0]["name"])
