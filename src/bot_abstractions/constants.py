
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

class BotMessages:
    NOT_IN_VC = 'You are not in a voice channel'
    JOINING_VC = "Joining Voice Channel..."
    ADDED_TO_QUEUE = "has been added to queue"
    QUEUE_CLEARED = 'Queue has been cleared'
    EMPTY_QUEUE = 'There are no songs in the queue'
    NOW_PLAYING = 'Now Playing: '

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

class ErrorMessages:
    DOWNLOAD_SONG_ERROR = "Problem occured while downloading the song"