import requests

url = 'http://127.0.0.1:8000/bot-users/list/'
myobj = {
    'telegram_id': 1232432,
    'username': 'sanjar',
    }

res = requests.post(url, json = myobj)

print(res.text)
