import requests, csv
from bs4 import BeautifulSoup

url = requests.get('https://id.carousell.com/categories/books-and-stationery-5')

soup = BeautifulSoup(url.text, 'html.parser')

books = soup.find('div', attrs={'class': 'D_s'})
populer = books.find_all('div', attrs={'class': 'D_aK'})

file = open('export_data.csv', 'w', newline='')
writer = csv.writer(file)
headers = ['Nama Toko', 'Nama Produk', 'Harga']
writer.writerow(headers)

for title in populer:
    nama_toko = (title.find('p', attrs={
        'class': 'D_su'}).text)
    produk  = (title.find('img')['title'])
    harga = (title.find('p', attrs={
        'class': 'D_sq'}).text)

    file = open('export_data.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    headers = ([nama_toko, produk, harga])
    writer.writerow(headers)
    file.close()