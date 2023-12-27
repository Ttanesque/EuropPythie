from interactions import Client, Intents, listen
from log import main as log
from config import bot as bot_conf
import logging
import database

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

bot.load_extension("game")
bot.start(bot_conf["token"])
