#mm88x#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
import requests
import os
import threading
#mm88x#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
os.system('clear')
#mm88x#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
#mm88x#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
CHAT_ID = input("Enter Your Telegram ID : ")
BOT_TOKEN = input("Enter Your Telegram Token : ")
file =input('FILE IDS : ')
rfile = open(file, 'r')
#mm88x#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
os.system('clear')
#mm88x#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)
#mm88x#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def chr():                  												#xxxx
	while True:														#xxxx
	   uid=rfile.readline().split('\n')[0]						    #xxxx
	   res = requests.get(f'http://instaup.marsapi.com/get_likes/shop/daily_coins?user_id={uid}').json()
	   coin = int(res['return']['coins'])
	   if coin > 400:
	       print(f'{E}[✅] : {G}{uid} {S}| {G}{coin}')	#@c533c
	       send_to_telegram(f'{uid} ==> {coin}\n')
	   elif coin < 400:
	   	print(f'{E}[❌] : {E}{uid} {B}| {E}{coin}')

if __name__ == '__main__':										#xxxx
    for _ in range(200):											   #xxxx
        threading.Thread(target=chr).start()					#xxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#mm88x#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx