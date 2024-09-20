import requests
from bs4 import BeautifulSoup
req = requests.get("https://practice.geeksforgeeks.org/")

soup = BeautifulSoup(req.content,"html.parser")

# print(soup.prettify())
print(soup.get_text())
# this is used for the web scrapping  as we can retrieve all the data from the specific website
res = soup.title
print(res.prettify())