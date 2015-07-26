import configparser

config = configparser.ConfigParser()
config.read("../../config.ini")

if "database" not in config or "path" not in config["database"]:
    raise ValueError("Database section not defined in config file!")

if "slack" not in config or "token" not in config["slack"]:
    raise ValueError("Slack section not defined in config file!")
