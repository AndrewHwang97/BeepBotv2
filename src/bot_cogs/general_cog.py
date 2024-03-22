import discord
from discord.ext import commands
from bot_abstractions.bot_constants import BotCommands, ErrorMessages
from bot_abstractions.bot_messages import BotMessages, EightBallResponses
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
    
    @commands.command(BotCommands.EIGHT_BALL)
    async def eight_ball(self, ctx):
        response_index = random.randint(0, 2) # Yes, No, Maybe
        try:
            if response_index == 0:
                index = random.randint(0, len(EightBallResponses.YES_STRINGS) - 1)
                await ctx.send(EightBallResponses.YES_STRINGS[index])
            elif response_index == 1:
                index = random.randint(0, len(EightBallResponses.NO_STRINGS) - 1)
                await ctx.send(EightBallResponses.NO_STRINGS[index])
            else:
                index = random.randint(0, len(EightBallResponses.MAYBE_STRINGS) - 1)
                await ctx.send(EightBallResponses.MAYBE_STRINGS[index])
        except:
            ctx.send(ErrorMessages.EIGHT_BALL_ERROR)