#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

import os
import requests 
import telegram
import asyncio
import glob
import time
##Telegram Data input#
TOKEN = "6654061760:AAH0PGZM8wfqFVJNAdy_ZAs6ou97A9kPX1U"
chat_id = "284515456"
bot = telegram.Bot(token=TOKEN)
#Template of searching#
path = '/Volumes/Transcend/Scripts/Send audio via Telegram from Asterisk/monitor/**/in-78312889797*.wav'
#Instalazing glob variable, path of searching and method of search###
inVar = glob.iglob(path, recursive = True)
#Starting a cycle. Create file with search result###
for result in inVar:
    file = open('pathAudio.txt', 'a+')
    file.write(result + '\n')
    file.close()
#Reading file with search content###
file = open('pathAudio.txt', 'r+')
pathContent1 = None
#Starting cycle to read by line file with search result###
while True:
    fileContent = file.readline()
    if not fileContent:
        break
    pathContent1 = fileContent.strip() #delete "\n" symbol from the string
#    time.sleep(2)
    async def sendAudio():
        await bot.sendAudio(chat_id=chat_id, audio=pathContent1)
    asyncio.get_event_loop().run_until_complete(sendAudio())
file.close()
os.remove('pathAudio.txt')
