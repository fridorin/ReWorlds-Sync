import logging
import disnake
from disnake.ext import commands
from utils.synchronization import synchronization_nicknames_guild

logger = logging.getLogger(__name__)


class Synchronization(commands.Cog):
    def __init__(self, bot: disnake.ext.commands.Bot):
        self.bot = bot

    @commands.slash_command(guild_only=True)
    @commands.has_permissions(manage_nicknames=True)
    async def synchronization(self, inter: disnake.ApplicationCommandInteraction,
                              member: disnake.Member = commands.Param(default=None)):
        await inter.response.defer(ephemeral=True)
        await inter.edit_original_response(
            embed=disnake.Embed(
                title="СИНХРОНИЗАЦИЯ",
                color=disnake.Color.orange(),
            )
        )
        if member is None:
            await synchronization_nicknames_guild(self.bot, inter.guild)
        else:
            await synchronization_nicknames_guild(self.bot, inter.guild, user=member)
        await inter.edit_original_response(
            embed=disnake.Embed(
                title="СИНХРОНИЗАЦИЯ",
                description="Успешно",
                color=disnake.Color.orange(),
            )
        )


def setup(bot: commands.Bot):
    bot.add_cog(Synchronization(bot))
    logger.info(f">{__name__} is launched")