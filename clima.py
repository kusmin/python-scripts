import requests
from bs4 import BeautifulSoup

# Carrega pagina com informações sobre o clime
html = requests.get(
    "https://www.climatempo.com.br/previsao-do-tempo/cidade/107/belohorizonte-mg").content

# faz parse do html da pagina
soup = BeautifulSoup(html, 'html.parser')


# captura dos dados navegando nos elementos do html
resume = soup.find(class_='-gray -line-height-24 _center')
tempMin = soup.find(id='min-temp-1')
tempMax = soup.find(id='max-temp-1')

# mostra resultados
print('\n Resumo: ' + resume.text)
print('Temp Minima: ' + tempMin.string)
print('Temp Maxima: ' + tempMax.string)
