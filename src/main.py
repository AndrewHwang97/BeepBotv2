import asyncio
import discord
from discord.ext import commands
from bot_cogs.music_cog import Music
from bot_cogs.general_cog import General
from bot_cogs.image_search_cog import ImageSearch
from bot_cogs.fight_cog import Fight
import os

bot = commands.Bot(command_prefix='/', intents = discord.Intents.all())

async def main():
    await bot.add_cog(Music(bot))
    await bot.add_cog(General(bot))
    await bot.add_cog(ImageSearch(bot))
    await bot.add_cog(Fight(bot))

asyncio.run(main())
bot.run(os.getenv("TOKEN"))