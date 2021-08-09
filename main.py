import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/populer')
def populer():
    url = requests.get('https://id.carousell.com/categories/books-and-stationery-5')

    soup = BeautifulSoup(url.text, 'html.parser')

    books = soup.find('div', attrs={'class': 'D_s'})
    populer = books.find_all('div', attrs={'class': 'D_aK'})

    return render_template('populer.html', populer=populer)

if __name__ == '__main__':
    app.run(debug=True)