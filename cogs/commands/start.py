import logging
import disnake
from disnake.ext import commands
from utils.database import initial_data_addition

logger = logging.getLogger(__name__)


class Start(commands.Cog):
    def __init__(self, bot: disnake.ext.commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def start(self, inter: disnake.ApplicationCommandInteraction):
        await initial_data_addition(1179812788911227040)


def setup(bot: commands.Bot):
    bot.add_cog(Start(bot))
    logger.info(f">{__name__} is launched")
