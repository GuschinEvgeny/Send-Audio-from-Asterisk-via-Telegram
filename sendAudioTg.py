import os
import requests 
import sys 
import pymssql 
import telegram
import asyncio
import glob as gb

TOKEN = "YOUR_BOT_TOKEN"
chat_id = "YOUR_TG_ID"
bot = telegram.Bot(token=TOKEN)
message = '/Volumes/Transcend/Scripts/Send audio via Telegram from Asterisk/monitor/2023/10/13/in-78312889797-3030-20231013-111501-1697184899.686.wav'

async def send_audio():
    await bot.send_audio(chat_id=chat_id,
                           audio= message,
                           )

asyncio.run(send_audio())

