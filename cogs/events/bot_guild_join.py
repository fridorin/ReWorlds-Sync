import logging
import disnake
from disnake.ext import commands
from utils.database import create_table

logger = logging.getLogger(__name__)


class BotJoin(commands.Cog):
    def __init__(self, bot: disnake.ext.commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await create_table(guild.id)


def setup(bot: commands.bot):
    bot.add_cog(BotJoin(bot))
    logger.info(f">{__name__} is launched")
