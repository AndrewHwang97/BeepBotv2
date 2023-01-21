import discord
from discord.ext import commands, tasks
from bot_abstractions.constants import YDLConstants, FfmpegConstants, Constants, BotMessages, BotCommands, ErrorMessages
from youtube_dl import YoutubeDL

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.song_queue = []
        self.song_title_list = []
        self.is_playing = False
        self.is_joined = False
        self.now_playing = ''
        self.Ydl_Options = {YDLConstants.FORMAT: YDLConstants.BESTAUDIO, YDLConstants.NO_PLAYLIST: YDLConstants.NO_PLAYLIST_SETTING}
        self.Ffmpeg_Options = {FfmpegConstants.BEFORE_OPTIONS: FfmpegConstants.BEFORE_OPTIONS_SETTINGS, FfmpegConstants.OPTIONS: FfmpegConstants.VN}
    
    async def play_song(self, ctx, user_input):
        if not self.is_joined:
            await self.join(ctx)
        
        if self.is_playing:
            await self.stop(ctx)
            print('DEBUG: stopping')
        
        voice_client = ctx.voice_client
        song = await self.prep_song_data(ctx, user_input)
        self.now_playing = song[Constants.TITLE]
        await ctx.send(BotMessages.NOW_PLAYING + f'{song[Constants.TITLE]}')
        self.is_playing = True
        voice_client.play(song[Constants.SOURCE], after=lambda e: self.play_next(ctx))
        self.check_if_playing.start(ctx)
    

    async def download_song(self, ctx, user_input):
        info = dict()
        with YoutubeDL(self.Ydl_Options) as ydl:
            try:
                if Constants.YOUTUBE_DOT_COM not in user_input:
                    #Search for song
                    info = ydl.extract_info(Constants.YT_SEARCH + f'{user_input}', download=False)[Constants.ENTRIES][0]
                else:
                    info = ydl.extract_info(user_input, download=False)
                song_title = info[Constants.TITLE]
                song_url = info[Constants.FORMATS][0][Constants.URL]
                source = await discord.FFmpegOpusAudio.from_probe(song_url, **self.Ffmpeg_Options)
                song=[(Constants.TITLE, song_title),(Constants.SOURCE, source)]
                return song
            except Exception as e:
                print(f'ERROR: {e}')
                await ctx.send(ErrorMessages.DOWNLOAD_SONG_ERROR)
    
    def play_next(self, ctx):
        voice_channel = ctx.voice_client
        if len(self.song_queue) > 0:
            source = self.song_queue.pop(0)
            self.now_playing = self.song_title_list.pop(0)
            self.is_playing = True
            voice_channel.play(source, after= lambda e: self.play_next(ctx))
        else:
            self.is_playing = False
            

    async def prep_song_data(self, ctx, user_input):
        song = await self.download_song(ctx, user_input)
        song = dict(song)
        return song
    
    async def add_to_queue(self, ctx, user_input):
        song = await self.prep_song_data(ctx, user_input)
        self.song_queue.append(song[Constants.SOURCE])
        self.song_title_list.append(song[Constants.TITLE])
        await ctx.send(f'{song[Constants.TITLE]} {BotMessages.ADDED_TO_QUEUE}')


    @tasks.loop(minutes = 3)
    async def check_if_playing(self, ctx):
        if self.is_playing == False and self.is_joined == True:
            await self.disconnect(ctx)

    
    @commands.command(BotCommands.JOIN)
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(BotMessages.NOT_IN_VC)
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            self.is_joined = True
            await ctx.send(BotMessages.JOINING_VC)
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
    
    @commands.command(BotCommands.DISCONNECT)
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
        self.song_queue = []
        self.is_joined = False
        self.check_if_playing.cancel()
    
    @commands.command(BotCommands.PAUSE)
    async def pause(self, ctx):
        ctx.voice_client.pause()

    @commands.command(BotCommands.SKIP, aliases = [BotCommands.FORCESKIP])
    async def skip(self, ctx):
        if len(self.song_queue) > 0:
            await self.stop(ctx)
        else:
            if self.is_playing:
                await self.stop(ctx)
    
    @commands.command(BotCommands.CLEAR)
    async def clear(self, ctx):
        self.song_queue = []
        self. song_title_list = []
        await ctx.send(BotMessages.QUEUE_CLEARED)
    
    @commands.command(BotCommands.QUEUE)
    async def queue(self, ctx):
        if len(self.song_queue) > 0:
            count = 0
            res = '```'
            for title in self.song_title_list:
                count += 1
                res += f'{str(count)}) {title}\n'
            res += '```'
            await ctx.send(res)
        else:
            await ctx.send(BotMessages.EMPTY_QUEUE)
    
    @commands.command(BotCommands.RESUME)
    async def resume(self, ctx):
        ctx.voice_client.resume()
    
    @commands.command(BotCommands.STOP)
    async def stop(self, ctx):
        self.is_playing = False
        ctx.voice_client.stop()
    
    @commands.command(BotCommands.PLAY)
    async def play(self, ctx, *user_input):
        search_string = ''
        if len(user_input) > 1:
            #if searching for a song 
            search_string = ' '.join(user_input)
        else:
            #if user_input is link itself
            search_string = user_input[0]
        
        if self.is_playing:
            await self.add_to_queue(ctx, search_string)
        else:
            await self.play_song(ctx, search_string)
