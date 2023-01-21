import asyncio
import discord
from discord.ext import commands
from bot_cogs.music_cog import Music
import os

bot = commands.Bot(command_prefix='/', intents = discord.Intents.all())

async def main():
    await bot.add_cog(Music(bot))

asyncio.run(main())
bot.run('MTA2NjQwNDEzOTY5MDYzNTMxNQ.G_Fqi4.DSqGQKVnxgKDfvTlX44D7o1hB9JZyIprrEtTu8')