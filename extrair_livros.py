# Importando as bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display

# Definir o cabeçalho com User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0 Safari/537.36"
}

# Criando lista para armazenar os dados
lista = []

# Percorrendo as 50 páginas
for pagina in range(1, 51):

    print(f"Processando página {pagina}...")

    # Definindo a URL de acordo com a página
    if pagina == 1:
        url = 'https://books.toscrape.com/'
    else:
        url = f'https://books.toscrape.com/catalogue/page-{pagina}.html'

    # Requisição GET para a página dos livros
    response = requests.get(url, headers=headers)

    # Extraindo o HTML
    html = response.text

    # Analisando com BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Identificando onde estão os livros
    livros = soup.find('ol').find_all('li')

    if livros:

        for livro in livros:

            # Criando um dicionário para cada livro
            dados = {}

            dados['Titulo'] = livro.find('h3').find('a')['title']

            dados['Preco'] = float(
                livro.find('p', class_='price_color')
                .get_text()
                .replace('Â£', '')
            )

            dados['Disponibilidade'] = (
                "Em estoque"
                if livro.find('p', class_='instock availability')
                .get_text(strip=True) == "In stock"
                else "Fora de estoque"
            )

            # Adiciona o livro na lista
            lista.append(dados)


# Mostra todos os livros coletados
print(f"\nTotal de livros coletados: {len(lista)}")

# Criando o DataFrame
df = pd.DataFrame(lista)

# Exibindo as primeiras linhas
display(df.head())

# Salvando em CSV
df.to_csv(
     #caminho do arquivo na pasta do drive,
    index=False
)