import logging
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
import log
from bot import ReworldsSync

load_dotenv(find_dotenv())
log.setup()

loop = asyncio.get_event_loop()
bot = ReworldsSync.create()
logger = logging.getLogger(__name__)

bot.load_extensions("cogs")
bot.run(os.getenv("TOKEN"))
