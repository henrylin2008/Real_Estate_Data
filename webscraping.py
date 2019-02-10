import requests
from bs4 import BeautifulSoup


r=requests.get("http://pythonhow.com/example.html")
c=r.content

# Display file in html format
soup=BeautifulSoup(c,"html.parser")

# Find all Div tags that has value of class: cities; 
# <div <div class="cities">
# <h2>London</h2>
# <p>London is the capital of England and it's been a British settlement since 2000 years ago. </p>
# </div> 

all=soup.find_all("div",{"class":"cities"})

# Find first Div tag that has value of class: cities
# all=soup.find("div",{"class":"cities"})
# or all=soup.find_all("div",{"class":"cities"})[0]

# [<h2>London</h2>]
all[0].find_all("h2")

# 'London'
all[0].find_all("h2")[0].text

# London
# Paris
# Tokyo
for item in all: 
	print(item.find_all("h2")[0].text)

# London is the capital of England and it's been a British settlement since 2000 years ago. 
# Paris is the capital city of France. It was declared capital since 508.
# Tokyo is the capital of Japan and one of the most populated cities in the world.
for item in all:
	print(item.find_all("p")[0].text)

