# Plugin to show the feds you are banned in.
# For TeleBot
# Kangers keep credits
# By @Akash_AM1 and @xditya

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME

naam = str(ALIVE_NAME)

bot = "@MissRose_bot"

@borg.on(admin_cmd(sudo_cmd(pattern="fstat ?(.*)")))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/fedstat")
              audio = await conv.get_response()
              final = ("If you would like to know more about the fedban reason in a specific federation, use /fbanstat <FedID> in RoseBot." , "")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @MissRose_Bot `and retry!")
    elif "@" in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/fedstat " + sysarg)
              audio = await conv.get_response()
              final = ("If you would like to know more about the fedban reason in a specific federation, use /fbanstat <FedID> in RoseBot." , "")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @MissRose_Bot `and try again!")
