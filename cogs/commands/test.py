import logging
import disnake
import time
from disnake.ext import commands
from utils.synchronization import synchronization_nicknames

logger = logging.getLogger(__name__)


class Test(commands.Cog):
    def __init__(self, bot: disnake.ext.commands.Bot):
        self.bot = bot

    @commands.slash_command(description="тестирирование")
    @commands.is_owner()
    async def test(self, inter: disnake.ApplicationCommandInteraction):
        start_time = time.time()
        await synchronization_nicknames(self.bot)
        end_time = time.time()
        await inter.response.send_message(
            embed=disnake.Embed(
                title="Время выполнения синхронизации",
                description=f"{end_time - start_time} секунд",
                color=disnake.Color.green(),
            ),
            ephemeral=True,
        )


def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))
    logger.info(f">{__name__} is launched")
