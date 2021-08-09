import requests
from bs4 import BeautifulSoup

url = requests.get('https://id.carousell.com/categories/books-and-stationery-5')

soup = BeautifulSoup(url.text, 'html.parser')

books = soup.find('div', attrs={'class': 'D_s'})
populer = books.find_all('div', attrs={'class': 'D_aK'})

for img in populer:
    produk = img.find('img')['title']
    image = img.find('img')['src']
    print(image)

    with open('images/' + produk + '.jpg', 'wb') as f:
        img = requests.get(image)
        f.write(img.content)
