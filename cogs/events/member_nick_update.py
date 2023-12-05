import logging
import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
main_guild_id = os.getenv("MAIN_GUILD_ID")
logger = logging.getLogger(__name__)


class MemberUpdate(commands.Cog):
    def __init__(self, bot: disnake.ext.commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before: disnake.Member, after: disnake.Member):
        if before.guild.id == int(main_guild_id):
            if before.nick != after.nick:
                for guild in self.bot.guilds:
                    if guild.id != main_guild_id:
                        for member in guild.members:
                            try:
                                if not member.bot:
                                    if before.id == member.id:
                                        await member.edit(nick=after.nick)
                            except disnake.Forbidden:
                                pass


def setup(bot: commands.bot):
    bot.add_cog(MemberUpdate(bot))
    logger.info(f">{__name__} is launched")
