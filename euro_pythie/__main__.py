import logging as log
from interactions import Client, Intents, listen
import database

log.basicConfig(encoding="utf-8", format='%(asctime)s %(levelname)s: %(message)s', level=log.DEBUG)
log.info("Initilization of EuroPythie")

bot = Client(
        intents=Intents.DEFAULT,
        sync_interactions=True,
        asyncio_debug=True,
        logger=log.getLogger("Interactions")
)

@listen()
async def on_ready():
    log.info("EuroPythie is ready")

database.init()

bot.load_extension("game")
bot.start("NjA5NzQ1MDAyNTkxMDI3MjIw.GtDQSO.CyLzHvLD4e2IjZ7qe5UfPiNiPiR8iO8K61_Nto")
