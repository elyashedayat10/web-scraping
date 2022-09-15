import requests
from bs4 import BeautifulSoup

username = 'elyashedayat10'
url = "https://github.com/{}"

parameters = {'tab': 'repositories'}
response = requests.get(url=url.format(username), params=parameters)
content = BeautifulSoup(response.text, 'html.parser')
repo_list = content.find(attrs={'id': 'user-repositories-list'})

final_result = []

for repo in repo_list.find_all('li'):
    repo_name = repo.find('h3').find('a').get_text(strip=True)
    repo_language = repo.find('span', attrs={'itemprop': 'programmingLanguage'})
    repo_language = repo_language.get_text(strip=True) if repo_language else 'No Language'
    repo_description = repo.find('p', attrs={'itemprop': 'description'})
    repo_description = repo_description.get_text() if repo_description else 'No Description'

    final_result.append({
        'repo_name': repo_name,
        'repo_language': repo_language,
        'repo_description': repo_description,
    })

for result in final_result:
    print(result)
