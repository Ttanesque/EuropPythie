from interactions import Client, Intents, listen
import logging
import database
import tomllib
from log import main as log 

log.info("Initilization of EuroPythie")

bot = Client(
    intents=Intents.DEFAULT,
    sync_interactions=True,
    asyncio_debug=True,
    logger=logging.getLogger("Interactions"),
)


@listen()
async def on_ready():
    log.info("EuroPythie is ready")


database.init()

with open("config.toml", "rb") as c:
    config = tomllib.load(c)

bot.load_extension("game")
bot.start(config["token"])
