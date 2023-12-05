import logging
import disnake
from disnake.ext import commands

logger = logging.getLogger(__name__)


class Activation(commands.Cog):
    def __init__(self, bot: disnake.ext.commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def activation(self, inter: disnake.ApplicationCommandInteraction, guild_id: int):
        await inter.response.send_message(
            embed=disnake.Embed(
                title="**ПИНГ БОТА**",
                description=f"{round(self.bot.latency * 1000)}ms",
                color=disnake.Color.green(),
            ),
            ephemeral=True,
        )


def setup(bot: commands.Bot):
    bot.add_cog(Activation(bot))
    logger.info(f">{__name__} is launched")