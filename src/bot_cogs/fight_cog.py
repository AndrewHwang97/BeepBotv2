import discord
from discord.ext import commands
from bot_abstractions.bot_constants import BotCommands, ErrorMessages
from bot_abstractions.bot_messages import BotMessages, FightResponses
import random

class Fight(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(BotCommands.FIGHT)
    async def fight(self, ctx, personToFight):
        if ctx.message.author == personToFight:
            print("why are you fighting yourself")      

        resIndex = random.randint(0, 2) # 0-p1 wins, 1-p2 wins, 2-tie
        res = ''
        match resIndex:
            case 0:
                res = await self.getResult(ctx.author.mention, personToFight, False)
            case 1:
                res = await self.getResult(personToFight, ctx.author.mention, False)
            case 2:
                res = await self.getResult(ctx.author.mention, personToFight, True)
        
        await ctx.send(res)

    async def getResult(self, person1, person2, isTie):
        resultString = ''
        if isTie:
            response_index = random.randint(0, len(FightResponses.TIE_RESPONSES) - 1)
            resultString = FightResponses.TIE_RESPONSES[response_index].format(person1, person2)
        else:
            response_index = random.randint(0, len(FightResponses.WIN_RESPONSES) - 1)
            resultString = FightResponses.WIN_RESPONSES[response_index].format(person1, person2)
        return resultString
        