#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

import os
import requests
import sys
import pymssql
import telegram
import asyncio
import glob
import time
#start comparison of current time whith creation time

def timeComparison(result):
    currentTime = int(time.time())
    creatFileTime = os.stat(result).st_mtime
    dayCount = 300
    daySeconds = 86400
    secondsDayCount = dayCount * daySeconds
    comparisonPeriod = currentTime - secondsDayCount
    if creatFileTime > comparisonPeriod:
        file.write(result + '\n')

path = '/Volumes/Transcend/Scripts/Send audio via Telegram from Asterisk/monitor/**/in-78312889797*.wav'

file = open('pathAudio', 'w')
inVar = glob.iglob(path, recursive = True)
for result in inVar:
    currentSize = os.stat(result).st_size
    if currentSize > 51200:      #comparison of empty file or not empty 
        timeComparison(result)

file.close()


##Telegram Data input#
TOKEN = "6654061760:AAH0PGZM8wfqFVJNAdy_ZAs6ou97A9kPX1U"
chat_id = "284515456"
bot = telegram.Bot(token=TOKEN)


file = open('pathAudio', 'r')
fileContent = file.readlines()
file.close()

pathContent1 = None

for pathContent1 in fileContent:
    pathContent1=pathContent1.strip()

## Send via Telegram
    async def sendAudio():
         await bot.sendAudio(chat_id=chat_id, audio=open(pathContent1, 'rb'))
    asyncio.get_event_loop().run_until_complete(sendAudio())

os.remove('pathAudio')