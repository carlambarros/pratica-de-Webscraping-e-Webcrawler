import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0 Safari/537.36"
}

url = "https://www.todamateria.com.br/estados-do-brasil"

response = requests.get(url, headers=headers)


html = response.content

soup = BeautifulSoup(html, "html.parser")

soup.prettify()

tables = soup.find_all("table")
print(len(tables))

table = tables[0]

for row in table.find_all("tr"):
    headers_cells = row.find_all(["th", "td"])

    if len(headers_cells) > 1:
        cabecalhos = [
            cell.get_text(strip=True).replace("\n", "")
            for cell in headers_cells
        ]
        break

rows = []

for row in table.find_all("tr"):
    cells = row.find_all(["th", "td"])

    if cells:
        row_data = [
            cell.get_text(strip=True)
            for cell in cells
        ]

        if len(row_data) == len(cabecalhos):
            rows.append(row_data)

df = pd.DataFrame(rows, columns=cabecalhos)

display(df.head())

df.to_csv(
     #caminho do arquivo na pasta do drive,
    index=False
)

df.to_excel(
     #caminho do arquivo na pasta do drive,
    index=False,
    engine="openpyxl"
)

print("Arquivos salvos com sucesso!")