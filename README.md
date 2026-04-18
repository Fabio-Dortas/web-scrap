Web Scraping com Python
Este projeto é um exemplo simples de web scraping utilizando as bibliotecas rich, requests e BeautifulSoup. Ele permite que o usuário insira um link e receba como saída os primeiros 30 textos de links (<a>) encontrados na página.

Funcionalidades
-Recebe um link do usuário via input.
-Faz uma requisição HTTP com cabeçalho de User-Agent.
-Utiliza BeautifulSoup para analisar o HTML.
-Extrai e imprime os textos dos links encontrados (limitado a 30 para evitar excesso).

Tecnologias utilizadas
-Python 3
-Requests
-BeautifulSoup (bs4)

Pré-requisitos
-Certifique-se de ter o Python instalado e instale as dependências:
Código => pip install requests beautifulsoup4

Como usar
Clone este repositório:

Código
git clone https://github.com/Fabio-Dortas/web-scrap.git

Acesse a pasta do projeto:

Código
cd web-scrap
Execute o script:

Código
python scraper.py
Digite o link da página quando solicitado.

Exemplo de uso
Código
Digite o link da página que deseja fazer scraping: https://example.com
Saída esperada:

Código
Home
Sobre
Contato
Blog
...
Aviso
Este projeto é apenas para fins educacionais. Respeite sempre os termos de uso e o arquivo robots.txt dos sites que você deseja acessar. Não utilize scraping para fins ilegais ou que violem direitos autorais.

Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
