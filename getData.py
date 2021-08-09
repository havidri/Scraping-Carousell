import requests
from bs4 import BeautifulSoup

url = requests.get('https://id.carousell.com/categories/books-and-stationery-5')

soup = BeautifulSoup(url.text, 'html.parser')

books = soup.find('div', attrs={'class': 'D_s'})
populer = books.find_all('div', attrs={'class': 'D_aK'})

for populers in populer:
    print('Nama Toko: ', populers.find('p', attrs={
        'class': 'D_su'}).text)
    print('Nama Product: ', populers.find('img')['title'])
    print('Image Product: ', populers.find('img')['src'])
    print('Harga Produk: ', populers.find('p', attrs={
        'class': 'D_sq'}).text)
