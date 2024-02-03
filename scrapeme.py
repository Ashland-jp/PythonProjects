import requests
from bs4 import BeautifulSoup

# set url with user input
url = input("Enter the URL you would like to scrape...  ")

# send HTTP request to URl and retrieve content
response = requests.get(url)

# create a beautifulsoup object that parses html data
soup = BeautifulSoup(response.content, 'html.parser')

# find all links on website

links = soup.find_all('a')

# print text and href attribute for each link
for link in links:
    print(link.get('href'), link.text)