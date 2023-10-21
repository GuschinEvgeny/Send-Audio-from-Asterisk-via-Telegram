import requests 
import sys 
import pymssql 
import telegram
import asyncio
import glob
 
path = '//monitor/**/*.wav'
inVar = glob.iglob(path, recursive = True) 
print(type(inVar)) 
for audio in inVar:
    print(audio)

TOKEN = "YOUR_BOT_TOKEN"
chat_id = "YOUR_TG_ID"
bot = telegram.Bot(token=TOKEN)
message = audio

async def send_audio():
    await bot.send_audio(chat_id=chat_id,
                           audio= message,
                           )
asyncio.run(send_audio())

