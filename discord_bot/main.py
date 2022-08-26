import asyncio
import os
from discord import Intents
from discord.ext import commands

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start('MTAxMTM3NTU0MDM4NjY2ODU3NA.GcQHE6.sRICCoLguqlVK6N3_7ads8217XK2AaM7vIlGL4')
asyncio.run(main())
