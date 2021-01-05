from bs4 import BeautifulSoup



html = open ("templates\products_list.html", 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
products = soup.find_all('a')
print(products.text.strip())
print(products.get('href'))
#product_list = []

#for product in products:
    #product_list.append({'name': product.text.strip(), 'link': product.get('href')})
#print(product_list)


#for link in products:
    #links = [link.get('href')]
    #print(links)

#for tag in products:
    #tags = [tag.text.strip()]
    #print(tags)
