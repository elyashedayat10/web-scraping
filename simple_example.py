import requests
from bs4 import BeautifulSoup

# question1
"""
Write a Python program to test if a given page is found or not on the server
"""


def found_(*, link: str) -> str:
    response = requests.get(link)
    if response.status_code == 404:
        return response.reason
    return response.reason


# print(found_(link="https://github.com/elyashedayat10"))

# question2
"""
Write a Python program to download and display the content of robot.txt for en.wikipedia.org.
"""
url = "https://en.wikipedia.org/robots.txt"
response = requests.get(url=url)
content = BeautifulSoup(response.text, "html.parser")
# print(content)

# question3
"""
 Write a Python program to get the number of datasets currently listed on data.gov.
"""
response = requests.get("https://data.gov/")
content = BeautifulSoup(response.text, "html.parser")
datasets_count = (
    content.find("label", attrs={"for": "search-header"}).find("a").get_text(strip=True)
)
# simpler ways
# datasets_count = content.find('a', attrs={'href': 'metrics.html'}).get_text(strip=True)
# print(datasets_count)


# question4
"""
Write a Python program to display the name of the most recently added dataset on data.gov.
"""

response = requests.get("http://catalog.data.gov/dataset?q=&sort=metadata_created+desc")
content = BeautifulSoup(response.text, "html.parser")
result = content.select_one("h3.dataset-heading > a").get_text(strip=True)
# print(result)


# question5
"""
Write a Python program to extract h1 tag from example.com. 
"""

url = "http://example.com/"
response = requests.get(url)
content = BeautifulSoup(response.text, "html.parser")
result = content.find_all("h1")
# or
# result=content.select('h1')
# print(result)

# question6
"""
Write a Python program to extract and display all the header tags from en.wikipedia.org/wiki/Main_Page
"""
url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)
content = BeautifulSoup(response.text, "html.parser")
final_result = content.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
headers_tag_list = [html_tag for html_tag in final_result]
# print(*final_result, end="\n\n")
# print(headers_tag_list)


# question7
"""
Write a Python program to extract and display all the image links from en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer).
"""
url = "https://en.wikipedia.org/wiki/Peter_Jeffrey"
response = requests.get(url)
content = BeautifulSoup(response.text, "html.parser")
images = content.find_all("img")
final_result = [image["src"] for image in images]

# print(*final_result, sep='\n')

# question8
"""
Write a Python program to get 90 days of visits broken down by browser for all sites on data.gov
"""
r = requests.get("https://analytics.usa.gov/data/live/browsers.json")
# print(r.json()['totals']['browser'])

# question10
"""
Write a Python program to check whether a page contains a title or not
"""


def check_title(*, link: str) -> bool:
    response = requests.get(link)
    content = BeautifulSoup(response.text, "html.parser")
    return True if content.find("h1") else False


# print(check_title(link="https://www.w3resource.com/"))


# question11
"""
Write a Python program to list all language names and number of related articles in the order they appear in wikipedia.org
"""

response = requests.get("https://www.wikipedia.org/")
content = BeautifulSoup(response.text, "html.parser")
data_list = content.findAll("a", {"class": "link-box"})
# print(*data_list, sep='\n')

# question12
"""
Write a Python program to get the number of people visiting a U.S. government website right now.
"""
url = "https://analytics.usa.gov/data/live/realtime.json"
response = requests.get(url).json()
# print("Number of online user : {}".format(response['data'][0]['active_visitors']))
