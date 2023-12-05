import logging
import os
import asyncio
import aiomysql
from dotenv import load_dotenv, find_dotenv

logger = logging.getLogger()
load_dotenv(find_dotenv())
loop = asyncio.get_event_loop()


async def conection_mysql():
    return (await aiomysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        db='data',
        loop=loop
    ))


async def create_table(guild_id):
    conn = await conection_mysql()
    cur = await conn.cursor()
    await cur.execute(f"""CREATE TABLE `{guild_id}` (name VARCHAR(100), value BIGINT)""")


async def initial_data_addition(guild_id):
    conn = await conection_mysql()
    cur = await conn.cursor()
    await cur.execute(f"""INSERT INTO `1179812788911227040` VALUES ("activation", 0)""")
