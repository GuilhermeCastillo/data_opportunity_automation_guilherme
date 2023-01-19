from urllib import response
import requests
from bs4 import BeautifulSoup
import os


def get_pdf(base_url):
    page = requests.get(base_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    urls_pdf = []

    # Percore por todas as tags de "links" e filtra todos os links que contém arquivos pdf
    for a in soup.find_all('a', href=True):
        if a['href'].startswith("https") and a['href'].endswith(".pdf"):
            urls_pdf.append(a['href'])

    return urls_pdf


def write_file_local(urls, output_path="/home/guilherme/projects/data_opportunity_automation_guilherme/temp"):
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(output_path, os.path.basename(url))
            with open(file_path, 'wb') as f:
                f.write(response.content)
    return


if __name__ == '__main__':
    base_url = "https://www.gob.mx/conadesuca/documentos/dieproc-reportes-de-avance-de-produccion-ciclo-azucarero-2020-2021?state=published"
    urls_pdf = get_pdf(base_url)

    write_file_local(urls_pdf[1:6])
