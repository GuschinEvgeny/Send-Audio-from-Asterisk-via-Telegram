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
    currentTime = time.time()
    creatFileTime = os.stat(result).st_ctime
    dayCount = 300
    daySeconds = 86400
    secondsDayCount = dayCount * daySeconds
    comparisonPeriod = currentTime - secondsDayCount
    if creatFileTime > comparisonPeriod:
        file.write(result + '\n')
##Telegram Data input#                
TOKEN = "YOUR_BOT_TOKEN"
chat_id = "YOUR_TELEGRAM_ID"
bot = telegram.Bot(token=TOKEN)
#Template of searching#
path = 'Tepmlate_of search'
#Instalazing glob variable, path of searching and method of search#
inVar = glob.iglob(path, recursive = True)
#Starting a cycle. Create file with search result### 
for result in inVar:
    file = open('pathAudio', 'a+')
    currentSize = os.stat(result).st_size
    if currentSize > 51200:      #comparison of empty file or not empty B
        timeComparison(result)
file.close()
#Reading file with search content###
file = open('pathAudio', 'r+')
pathContent1 = None
#Starting cycle to read by line file with search result###
while True:
    fileContent = file.readline()
    if not fileContent:
        break
    pathContent1 = fileContent.strip() #delete "\n" symbol from the string
    print(pathContent1)
# Send via Telegram
    async def sendAudio():
        await bot.sendAudio(chat_id=chat_id, audio=pathContent1)
    asyncio.get_event_loop().run_until_complete(sendAudio())
file.close()
os.remove('pathAudio')



