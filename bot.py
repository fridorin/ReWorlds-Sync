import logging
import disnake
import traceback
from disnake.ext import commands
from utils.synchronization import synchronization_nicknames_all

logger = logging.getLogger()
owners = [852631483713585192]


class ReworldsSync(commands.Bot):
    @classmethod
    def create(cls) -> "ReworldsSync":
        return cls(
            owner_ids=set(owners),
            status=disnake.Status.online,
            intents=disnake.Intents.all(),
            command_prefix="!",
            allowed_mentions=disnake.AllowedMentions(),
            activity=disnake.Game("синхронизирование"),
        )

    async def on_ready(self):
        logger.info(f"Logged in as {self.user.name}")
        try:
            await synchronization_nicknames_all(self)
        except Exception:
            logging.error(f"Произошла неизвестная ошибка: {traceback.format_exc()}")