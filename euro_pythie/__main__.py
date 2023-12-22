from interactions import Client, Intents, listen
import logging as log
import database
import tomllib

log.basicConfig(
    encoding="utf-8", format="%(asctime)s %(levelname)s: %(message)s", level=log.DEBUG
)
log.info("Initilization of EuroPythie")

bot = Client(
    intents=Intents.DEFAULT,
    sync_interactions=True,
    asyncio_debug=True,
    logger=log.getLogger("Interactions"),
)


@listen()
async def on_ready():
    log.info("EuroPythie is ready")


database.init()

with open("config.toml", "rb") as c:
    config = tomllib.load(c)

bot.load_extension("game")
bot.start(config["token"])
