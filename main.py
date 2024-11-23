import json

with open("config.json") as f:
	config = json.load(f)


if config["users"][0]["age"] < 18:
	exit("Пользователям до 18 нельзя!" if config["lang"] == "ru" else "no users under 18!")

print("привет мир," if config["lang"] == "ru" else "hello world, ", config["users"][0]["name"], "!")

