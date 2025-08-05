from bs4 import BeautifulSoup
import requests

url = 'https://listado.mercadolibre.com.pe/zapatillas-hombre#D[A:zapatillas%20hombre]'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

if response.status_code == 200:
    print("Página accedida correctamente")
    soup = BeautifulSoup(response.text, 'html.parser')
    # products = soup.find_all('div', class_='li.ui-search-layout__item')
    # products = soup.find_all('div', class_='andes-card andes-card--flat andes-card--padding-0 andes-card--animated')
    products = soup.find_all('div', class_='andes-card poly-card poly-card--grid-card poly-card--large poly-card--CORE andes-card--flat andes-card--padding-0 andes-card--animated')
    # print(len(products))
else:
    print(f"Error al acceder a la página: {response.status_code}")

