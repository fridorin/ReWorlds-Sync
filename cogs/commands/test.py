import logging
import disnake
import time
from disnake.ext import commands

from utils.database import create_table, initial_data_addition
from utils.synchronization import synchronization_nicknames_all

logger = logging.getLogger(__name__)


class Test(commands.Cog):
    def __init__(self, bot: disnake.ext.commands.Bot):
        self.bot = bot

    @commands.slash_command(description="тестирирование")
    @commands.is_owner()
    async def test(self, inter: disnake.ApplicationCommandInteraction):
        start_time = time.time()
        await create_table(1179812788911227040)
        end_time = time.time()
        print(end_time - start_time)


def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))
    logger.info(f">{__name__} is launched")
