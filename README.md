# BeepBotv2
Refactored version of BeepBot

## Overview
BeepBot is a music playing bot used on Discord that allows seamless audio playing to a voice channel with youtube links

## Commands
commands are executed using the following format when connected to a discord voice channel: <prefix><command> **args
| Command | Description |
| :---:   | :---: |
| join | Commands bot to join voice channel of input user |
| disconnect | Commands bot to disconnect from voice channel of input user |
| pause | Commands bot to pause audio if it is currently streaming audio |
| skip | Commands bot to skip the current audio file and starts next audio file in queue. stops audio streaming if queue is empty |
| clear | Clears Song Queue |
| queue | Sends a message to channel displaying queue list |
| resume | Resumes paused song |
| play {name of song} | conducts a youtube search based on input, downloads best matched youtube video |
| play {youtube link} | Plays audio from the youtube link |

## Extra Commands
commands that are not associated with playing music
| Command | Description |
| :---:   | :---: |
| 8ball {question} | Returns value from 8ball |
| scale {lowNumber}-{highNumber} {question} | Returns scale value from low to high (ex. scale 1-10 {question}) |
| image {word} | Posts an image related to the word. NSFW images are filtered out |
