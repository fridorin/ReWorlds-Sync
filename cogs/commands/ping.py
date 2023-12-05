import logging
import disnake
from disnake.ext import commands

logger = logging.getLogger(__name__)


class Ping(commands.Cog):
    def __init__(self, bot: disnake.ext.commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Проверить пинг бота")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            embed=disnake.Embed(
                title="**ПИНГ БОТА**",
                description=f"{round(self.bot.latency * 1000)}ms",
                color=disnake.Color.green(),
            ),
            ephemeral=True,
        )


def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))
    logger.info(f">{__name__} is launched")
