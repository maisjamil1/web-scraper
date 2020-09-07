import requests
from bs4 import BeautifulSoup
URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
page = requests.get(URL)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')# to convert the text to obj

print(soup)