import requests
from bs4 import BeautifulSoup

# 1. Receber o link do usuário
url = input("Digite o link da página que deseja fazer scraping: ")

# 2. Fazer requisição HTTP
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = soup.find_all('a')
    for link in links[:30]:  # limitar para não imprimir demais
        print(link.text.strip(),)
else:
    print("Erro ao acessar a página.")
