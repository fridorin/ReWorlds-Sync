import logging
import disnake
import asyncio
import traceback
from disnake.ext import commands
from utils.synchronization import synchronization_nicknames

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
