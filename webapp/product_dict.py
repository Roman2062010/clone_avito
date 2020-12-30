from bs4 import BeautifulSoup


html = open ("templates\products_list.html", 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
products = soup.find_all('a')

for link in products:
    links = [link.get('href')]
    print(links)

for tag in products:
    tags = [tag.text.strip()]
    print(tags)
