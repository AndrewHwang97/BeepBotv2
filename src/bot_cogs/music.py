import discord
from bot_abstractions.constants import YDLConstants, FfmpegConstants, Constants
from discord.ext import commands
from youtube_dl import YoutubeDL
import ffmpeg

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.is_playing = False
        self.is_paused = False

        self.song_queue = []
        self.YDL_OPTIONS = {YDLConstants.FORMAT: YDLConstants.BESTAUDIO}
        self.FFMPEG_OPTIONS = {FfmpegConstants.BEFORE_OPTIONS: FfmpegConstants.BEFORE_OPTIONS_SETTINGS, FfmpegConstants.OPTIONS: FfmpegConstants.VN }

        self.vc = None

    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False
        return {'source': info['formats'[0]['url']], 'title': info['title']}
    
    def play_next(self):
        if len(self.song_queue) > 0:
            self.is_playing = True

            song_url = self.song_queue[0][0][Constants.SOURCE]
            self.song_queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(song_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False
    
    async def play_song(self, ctx):

        if len(self.song_queue) > 0:
            self.is_playing = True
            song_url = self.song_queue[0][0][Constants.SOURCE]

            if self.vc == None or not self.vc.is_connected():
                self.vc = await self.song_queue[0][1].connect()

                if self.vc == None:
                    await ctx.send('There was a problem connecting to the voice channel')
                    return
                else:
                    await self.vc.move_to(self.song_queue[0][1])
                
                self.song_queue.pop()

                self.vc.play(discord.FFmpegPCMAudio(song_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False    