import os
import disnake
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
main_guild_id = os.getenv("MAIN_GUILD_ID")


async def synchronization_nicknames(client):
    main_guild = client.get_guild(int(main_guild_id))
    for number in f"{len(client.guilds)}":
        if client.guilds[int(number) - 1] != main_guild:
            for member in client.guilds[int(number) - 1].members:
                try:
                    if not member.bot:
                        main_member = main_guild.get_member(member.id)
                        try:
                            await member.edit(nick=main_member.nick)
                        except AttributeError:
                            try:
                                await member.edit(nick=main_member.display_name)
                            except AttributeError:
                                try:
                                    await member.edit(nick=main_member.name)
                                except AttributeError:
                                    pass
                except disnake.Forbidden:
                    pass
