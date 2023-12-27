import logging as log
import tomllib

with open("config.toml", "rb") as c:
    config = tomllib.load(c)

if config is None:
    log.error("Config is empty check if config.toml is present")

bot = config["EuroPythie"]
game = config["Game"]

log.info("Config ready")