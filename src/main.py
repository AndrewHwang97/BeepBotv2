import asyncio
import discord
from discord.ext import commands
from bot_cogs.music_cog import Music
from bot_cogs.general import General
import os

bot = commands.Bot(command_prefix='/', intents = discord.Intents.all())

async def main():
    await bot.add_cog(Music(bot))
    await bot.add_cog(General(bot))

asyncio.run(main())
bot.run(os.getenv("TOKEN"))