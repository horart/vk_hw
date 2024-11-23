import json

with open("config.json") as f:
	config = json.load(f)


if config["users"][0]["age"] < 18:
	exit("Users younger than 18 are not allowed!")

print("Hello world,", config["users"][0]["name"])

