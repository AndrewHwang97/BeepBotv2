import discord
from discord.ext import commands
from bot_abstractions.bot_constants import BotCommands, ErrorMessages
from bing_image_urls import bing_image_urls
import random

class ImageSearch(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(BotCommands.IMAGE)
    async def image_search(self, ctx, *input):
        try:
            search_string = ' '.join(input)
            search_results = bing_image_urls(search_string)
            image_index = random.randint(0, len(search_results) - 1)
            await ctx.send(search_results[image_index])
        except Exception as e:
            print(f'EXCEPTION: {e}')
            await ctx.send(ErrorMessages.IMAGE_SEARCH_ERROR)
