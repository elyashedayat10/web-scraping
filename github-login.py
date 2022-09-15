import requests
from bs4 import BeautifulSoup

session = requests.Session()

url = 'https://github.com/{}'


r = session.get(url.format('login'))
content = BeautifulSoup(r.text, 'html.parser')

data = {}
for form in content.find_all('form'):
    for inp in form.select('input[type=hidden]'):
        data[inp.get('name')] = inp.get('value')

data.update({'login': 'your username', 'password': 'your pass'})

r = session.post(url.format('session'), data=data)
print(r.reason)
