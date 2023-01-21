import discord
from discord.ext import commands
from bot_cogs.music import Music
from bot_cogs.general import General
import os

bot = commands.Bot(command_prefix='/')
bot.add_cog(Music(bot))
bot.add_cog(General(bot))

bot.run(os.getenv("TOKEN"))