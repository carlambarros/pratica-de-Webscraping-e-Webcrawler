import requests
from bs4 import BeautifulSoup
import os

url = 'https://frs.edu.br/wp-content/uploads/2025/05/'

response = requests.get(url)

# verificar se o site vai responder corretamente (200=ok)

if response.status_code == 200:
  #ler o html
  soup = BeautifulSoup(response.content, 'html.parser')

  # coletar os links da página
  links = soup.find_all('a')

  # local onde os PDFS serão salvos
  pasta_download = #caminho do arquivo na pasta do drive

  # caso não exista a página, vamos criar automaticamente
  os.makedirs(pasta_download, exist_ok=True)

  # percorrer todos os links
  for link in links:
    href = link.get('href')
    nome = link.text.strip()

  # verificar se é um arquivo png, jpg ou jpeg
    if href and href.endswith(('.png', 'jpg', 'jpeg')):
      #montar a url completa do arquivo
      arquivo_url = url + href

      # montar o caminho para salvar o arquivo
      caminho_arquivo = os.path.join(pasta_download, nome)

      # baixar o arquivo pdf
      print(f'Baixando: {nome}')
      resp_arq = requests.get(arquivo_url, stream =True)

      if resp_arq.status_code == 200:
        with open(caminho_arquivo, 'wb') as f:
          for chunk in resp_arq.iter_content(chunk_size=8192):
            f.write(chunk)
        print(f'Download concluído: {nome}')
      else:
        print(f'Erro ao baixar o arquivo: {nome}')
else:
  print('Erro ao acessar a página')