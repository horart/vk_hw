import json

with open("config.json") as f:
	config = json.load(f)


if config["users"][0]["age"] < 18:
	exit("Пользователям до 18 нельзя!")

print("Hello world,", config["users"][0]["name"])

