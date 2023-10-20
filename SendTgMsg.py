#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

import requests 
import sys 
import pymssql 
import telegram
import asyncio
from asterisk.agi import  AGI  

agi = AGI() 
phone = str(agi.env["agi_callerid"]) 
exten = str(agi.env["agi_extension"])
text = ' 🟢 <b>Incoming call from  </b> ' + exten + ' to ' + phone

#----------------для пробы строки ниже---------
TOKEN = "6654061760:AAH0PGZM8wfqFVJNAdy_ZAs6ou97A9kPX1U"
chat_id = "284515456"
bot = telegram.Bot(token=TOKEN)
message = text

async def send_message():
    await bot.send_message(chat_id=chat_id,
                           text= message,
                           parse_mode=telegram.constants.ParseMode.HTML)

asyncio.run(send_message())
asyncio.run(send_message2())
