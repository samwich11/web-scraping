from bs4 import BeautifulSoup
import requests

# Scrape the page: Scrape this site

# url = "https://www.scrapethissite.com/pages/forms"
url = "https://dockerlabs.es/"

respuesta = requests.get(url)

print(respuesta.status_code)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    maquinas = soup.find_all('div', onclick=True)
    conteo_maquinas = 0

    autores = set()

    for maquina in maquinas:
        onclick_text = maquina['onclick']
        autor = onclick_text.split("'")[7]
        autores.add(autor)        
        nombre_maquina = onclick_text.split("'")[1]
        conteo_maquinas += 1
        
    print(f"Autores encontrados: ")
    for autor in autores:
        print(autor)
    
    for maquina in maquinas:
        onclick_text = maquina['onclick']
        nombre = onclick_text.split("'")[1]
        dificultad = onclick_text.split("'")[3]
        autor = onclick_text.split("'")[7]

        print(f"{nombre} --> {dificultad} --> {autor}")
    
    # print(f"El número de máquinas encontradas es: {conteo_maquinas}")
else:
    print(f"Hubo un error al hacer la petición: {respuesta.status_code}")

# page = requests.get(url)
# print(page)

# status_code = page.status_code
# print(f"Status Code: {status_code}")

# soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())
