import asyncio
import discord
from discord.ext import commands
from bot_cogs.music_cog import Music
import os

bot = commands.Bot(command_prefix='/', intents = discord.Intents.all())

async def main():
    await bot.add_cog(Music(bot))

asyncio.run(main())
bot.run(os.getenv("TOKEN"))