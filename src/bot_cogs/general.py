import discord
from discord.ext import commands
from bot_abstractions.constants import BotMessages, BotCommands
import random


class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(BotCommands.HELLO)
    async def hi(self, ctx):
        index = random.randint(0, len(BotMessages.HELLO_STRINGS) - 1)
        await ctx.send(BotMessages.HELLO_STRINGS[index])
        
    @commands.command(BotCommands.SCALE)
    async def scale(self, ctx, scale):
        rnge = str.split(scale,'-')
        val = random.randint(int(rnge[0]), int(rnge[1]))
        await ctx.send(val)
        