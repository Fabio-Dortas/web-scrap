from bs4 import BeautifulSoup
from rich import print
from rich.panel import Panel
import requests


#1 Fazer requisição Url
url = input("Digite o link da página que deseja fazer scraping: ")

try:
    # 2. Fazer requisição HTTP
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})


    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    
        links = soup.find_all('a')
        for link in links[:30]:  # 3. limitar para não imprimir demais
            caixa = Panel(link.text.strip())
        print(caixa) # 4. Exibe resultados organizados em caixas
    else:
        print("Erro ao acessar a página.")

except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e) # 5. Tratamento de erros

except Exception as e:
    print("Erro inesperado:", e)
