import requests 
import sys 
import pymssql 
import telegram


#text = "Тестируем скрипт"
text = 'fileContent'
#text =  'Incoming call from: '  + exten + ' to ' + phone

#----------------для пробы строки ниже---------
#bot = telegram.Bot(token="6654061760:AAH0PGZM8wfqFVJNAdy_ZAs6ou97A9kPX1U")
#TOKEN = "6654061760:AAH0PGZM8wfqFVJNAdy_ZAs6ou97A9kPX1U"
#chat_id = "284515456"
#message = text
#url = f"https://api.telegram.org/bot{TOKEN}/sendFile?chat_id={chat_id}&audio={message}"
#print(requests.get(url).json())
#bot.send_message(chat_id="284515456", text= text)
#-------------модуль отправки выше с помощью функции print. Надой найти asterisk.agi

def main(text: str): 
    token = "6654061760:AAH0PGZM8wfqFVJNAdy_ZAs6ou97A9kPX1U" 
    url = "https://api.telegram.org/bot" 
    channel_id = "284515456" 
    url += token 
    method = url + "/sendMessage"  
    r = requests.post(method, data={ 
         "chat_id": channel_id,
         "text": text 
          })

    if r.status_code != 200: 
        raise Exception("post_text error")  
if __name__ == '__main__':
    main(text)




# print(requests.get(r).json())
# https://api.telegram.org/bot6654061760:AAH0PGZM8wfqFVJNAdy_ZAs6ou97A9kPX1U/sendMessage?chat_id=284515456&text=test
