import subprocess
import os
import requests


def send_image(image_path):
    url = "https://api.telegram.org/bot913916824:AAFMTGM7ZqaL-_YLOsyR4wPf6y9kmyI_NAc/sendPhoto";
    files = {'photo': open(image_path, 'rb')}
    data = {'chat_id' : "457034044"}
    r= requests.post(url, files=files, data=data)
    print(r.status_code, r.reason, r.content)

def send_text(bot_message):
    
    bot_token = '913916824:AAFMTGM7ZqaL-_YLOsyR4wPf6y9kmyI_NAc'
    bot_chatID = '457034044'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
send_text("BIRB ALERT")
send_image("/home/pi/Desktop/image_2.jpg")
