import requests
from bs4 import BeautifulSoup

url = "https://www.psck.net/album/list"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
tag_ans = soup.find_all('a')
print(tag_ans)
