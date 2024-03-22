
class YDLConstants:
    BESTAUDIO = 'bestaudio'
    FORMAT = 'format'
    NO_PLAYLIST = 'noplaylist'
    NO_PLAYLIST_SETTING = 'True'

class FfmpegConstants:
    BEFORE_OPTIONS = 'before_options'
    BEFORE_OPTIONS_SETTINGS = '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
    OPTIONS = 'options'
    VN = '-vn'

class Constants:
    SOURCE = 'source'
    TITLE = 'title'
    YOUTUBE_DOT_COM = 'www.youtube.com'
    YT_SEARCH = 'ytsearch:'
    ENTRIES = 'entries'
    FORMATS = 'formats'
    URL = 'url'

class BotCommands:
    JOIN = 'join'
    DISCONNECT = 'disconnect'
    PAUSE = 'pause'
    SKIP = 'skip'
    FORCESKIP = 'fs'
    CLEAR = 'clear'
    QUEUE = 'queue'
    RESUME = 'resume'
    STOP = 'stop'
    PLAY = 'play'
    HELLO = 'hi'
    SCALE = 'scale'
    EIGHT_BALL = '8ball'
    IMAGE = 'image'
    FIGHT = 'fight'

class ErrorMessages:
    DOWNLOAD_SONG_ERROR = "Problem occured while downloading the song"
    EIGHT_BALL_ERROR = "Oopsies, looks like there was a problem shaking the 8-ball. Try again"
    IMAGE_SEARCH_ERROR = "Oopsies, looks like there was a problem searching for the image"