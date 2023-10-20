import requests 
import sys 
import pymssql 
import telegram
import asyncio
import glob
 
path = '/Volumes/Transcend/Scripts/Send audio via Telegram from Asterisk/monitor/**/in-78312889797*.wav'
inVar = glob.iglob(path, recursive = True) 
print(type(inVar)) 
for audio in inVar:
    print(audio)

TOKEN = "6654061760:AAH0PGZM8wfqFVJNAdy_ZAs6ou97A9kPX1U"
chat_id = "284515456"
bot = telegram.Bot(token=TOKEN)
message = audio

async def send_audio():
    await bot.send_audio(chat_id=chat_id,
                           audio= message,
                           )
asyncio.run(send_audio())

