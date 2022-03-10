import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from NoinoiRobot.events import register as MEMEK
from NoinoiRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/4af36e1114f010b951e98.jpg"

@MEMEK(pattern=("/mhelp"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = (
      "** ──「 Basic Guide 」── ** \n\n" +
      "• /play **(song title) — To Play the song you requested via YouTube** \n"
  )
  LUNA += "• /search ** (song/video title) – To search for links on YouTube with details** \n"
  LUNA += "• /playlist - **show the list song in queue** \n"
  LUNA += "•/lyric - ** (song name) lyrics scrapper** \n\n"
  LUNA += "** ──「 Admin CMD 」── ** \n\n"
  LUNA += "• /pause - **To Pause Song playback** \n"
  LUNA += "• /resume - **To resume playback of the paused Song** \n"
  LUNA += "• /skip - **To Skip playback of the song to the next Song** \n"
  LUNA += "• /end - **To Stop Song playback** \n"
  LUNA += "• /control - **open the player settings panel** \n"
  LUNA += "• /reload - **To Refresh admin list** \n"

  BUTTON = [[Button.url("☎️ Support", "https://t.me/cfc_bot_support"), Button.url("📡 Updates", "https://t.me/bazigar_xd")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
