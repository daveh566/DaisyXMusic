# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**HELLO 👋 [{}](tg://user?id={})!**\n\n🤖 I AM A BOT FOR PLAYING MUSIC IN THE VOICE CHATS IN TELEGRAM GROUPS & CHANNELS.\n\n✅ SEND ME /help FOR MORE INFO."
      HELP_MSG = [
        ".",
f"""
**HEY  WELCOME 😊 BACK TO {PROJECT_NAME}

⚪️ {PROJECT_NAME} PLAYS MUSIC IN TELEGRAM GROUPS VCS AND PM

⚪️ ASSISTANT'S NAME >> @{ASSISTANT_NAME}\n\nClick NEXT FOR INSTRUCTIONS**
""",

f"""
**SETTING UP**

✓ MAKE BOT ADMIN (GROUP AND IN CHANNEL IF USE CPLAY)
✓ START A VOICE CHAT
✓ TRY /play [song name] FOR THE FIRST TIME (ADMIN)
*) IF USERBOT JOINED ENJOY MUSIC, IF NOT ADD @{ASSISTANT_NAME} TO YOUR GROUP 😁 AND RETRY

**FOR CHANNEL MUSIC PLAY**
✓ MAKE ME ADMIN OF YOUR CHANNEL 
✓ SEND /userbotjoinchannel IN LINKED GROUP
✓ NOW SEND COMMANDS IN LINKED GROUP 😁
""",
f"""
**COMMANDS**

**=>> SONG PLAYING 🎧**

- /play: PLAY THE REQUESTD SONG
- /play [yt url] : PLAY THE GIVEN YT URL
- /play [reply yo audio]: PLAY REPLIED AUDIO
- /dplay: PLAY SONG VIA DEEZER
- /splay: PLAY SONG VIA JIO SAAVN
- /ytplay: DIRECTLY PLAY SONG VIA YOUTUBE MUSIC

**=>> PLAYBACK ⏯**

- /player: OPEN SETTINGS MENU OF PLAYER
- /skip: SKIPS THE CURRENT TRACK
- /pause: PAUSE TRACK
- /resume: RESUMES THE PAUSED TRACK
- /end: STOPS MEDIA PLAYBACK
- /current: SHOWS THE CURRENT PLAYING TRACK
- /playlist: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",

f"""
**=>> CHANNEL MUSIC PLAY 🛠**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
- /cdplay [song name] - play song you requested via deezer
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
""",

f"""
**=>> MORE TOOLS 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
f"""
**=>> SONG DOWNLOAD 🎸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**=>> Search Tools 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",

f"""
**=>> COMMANDS FOR SUDO USERS ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
