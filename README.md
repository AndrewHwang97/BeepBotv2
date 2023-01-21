# BeepBotv2
Refactored version of BeepBot

## Overview
BeepBot is a music playing bot used on Discord that allows seamless audio playing to a voice channel with youtube links

## Commands
commands are executed using the following format when connected to a discord voice channel: !<command> **args
| Command | Description |
| :---:   | :---: |
| join | Commands bot to join voice channel of input user |
| disconnect | Commands bot to disconnect from voice channel of input user |
| pause | Commands bot to pause audio if it is currently streaming audio |
| skip | Commands bot to skip the current audio file and starts next audio file in queue. stops audio streaming if queue is empty |
| np | Displays current audio file playing |
| clear | Clears Song Queue |
| queue | Sends a message to channel displaying queue list |
| resume | Resumes paused song |
| play {name of song} | conducts a youtube search based on input, downloads best matched youtube video |
| play {youtube link} | Plays audio from the youtube link |
| play {youtube link with timestamp} | Plays audio form a youtube link starting at the timestamp in the link|
