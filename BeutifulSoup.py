import requests
from bs4 import BeutifulSoup
url = "https://www.codewithharry.com"

# Step 1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

# Step 2 : Parse the HTML
soup = BeutifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

# Step 3 : HTML tree traversal

# Get the title of the Html page
title=soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
#print(paras)

# Get all the anchor from the page
anchor = soup.find_all('a')
#print(anchor)

# Get first element from the HTML page
print(soup.find('p'))

# Get classes of any element from the HTML page
print(soup.find('p')['class'])

# find all the elements with class lead
print(soup.find_all("p",class_="lead"))

# Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

# Get all the links on the page
anchor = soup.find_all('a')
all_links = set()
for link in anchor:
    if(link.get('href') != '#'):
        linkText = "https://www.codewithharry.com"
        all_links.add(link)
        print(linkText)

# Get commet
markup = "<p><!-- this is a comment --></p>"
soup2= BeutifulSoup(markup)
print(type(soup2.p.string))

navbarSupportedContent = soup.find(id='navbarSupportedContent')
for elem in navbarSupportedContent.contents:
    print(elem)
exit()  

