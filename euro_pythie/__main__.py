from interactions import Client, Intents, listen
import logging
import database
import tomllib
from log import CustomFormatter

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())

logging.basicConfig(
    encoding="utf-8",
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.DEBUG,
    handlers=[ch],
)
log = logging.getLogger("Euro_pythie")

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
