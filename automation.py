import requests
from bs4 import BeautifulSoup
import os
from pdf_reader import PDF
import pandas as pd


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


def df_to_xlsx(df):
    df.to_csv('reportes.csv', index=False)
    df.to_excel('reportes.xlsx', sheet_name='Cuadro 7', index=False)
    os.remove(os.getcwd()+"/reportes.csv")
    return


base_url = "https://www.gob.mx/conadesuca/documentos/dieproc-reportes-de-avance-de-produccion-ciclo-azucarero-2020-2021?state=published"
# urls_pdf = get_pdf(base_url)
# write_file_local(urls_pdf[1:6])
dir_pdfs = os.getcwd()+'/temp'
list_pdfs = os.listdir(dir_pdfs)

list_df_final = []
for reporte in list_pdfs:
    pdf = PDF(dir_pdfs+"/"+reporte)
    page = pdf.search_index_table_by_title()

    list_df = []
    for i in range(0, 6):
        list_df.append(pdf.create_table(i, page))

    df_final = pd.concat(list_df, ignore_index=True)
    list_df_final.append(df_final)

df_final = pd.concat(list_df_final, ignore_index=True)
df_final = df_final.drop(columns=["Unnamed: 0", "Unnamed: 1", "Unnamed: 2"])

df_to_xlsx(df_final)

if __name__ == '__main__':
    ...
