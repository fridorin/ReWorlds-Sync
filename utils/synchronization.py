import os
import disnake
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
main_guild_id = os.getenv("MAIN_GUILD_ID")


async def synchronization_nicknames_all(client):
    main_guild = client.get_guild(int(main_guild_id))
    for guild in client.guilds:
        if guild.id != main_guild.id:
            for member in guild.members:
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


async def synchronization_nicknames_guild(client, guild, user=None):
    main_guild = client.get_guild(int(main_guild_id))
    if user is None:
        for member in guild.members:
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
    else:
        try:
            if not user.bot:
                main_member = main_guild.get_member(user.id)
                try:
                    await user.edit(nick=main_member.nick)
                except AttributeError:
                    try:
                        await user.edit(nick=main_member.display_name)
                    except AttributeError:
                        try:
                            await user.edit(nick=main_member.name)
                        except AttributeError:
                            pass
        except disnake.Forbidden:
            pass
