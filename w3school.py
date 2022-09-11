import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/python/python_lists_methods.asp"

response = requests.get(url)

content = BeautifulSoup(response.content, 'html.parser')

table = content.find_all('table', class_="ws-table-all notranslate")

for info in table:
    items = {}
    rows = info.findAll('tr')[2:]

    counter = 0
    for row in rows:
        items[counter] = {
            'url': row.find('td').find('a')['href'],
            'method': row.find('a').text,
            'description': row.findAll('td')[1].text
        }
        counter += 1

    for item in items.items():
        print(item)
        print("*" * 99)
