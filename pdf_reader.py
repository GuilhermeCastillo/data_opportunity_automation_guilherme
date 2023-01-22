import pandas as pd
import tabula
import numpy as np
import PyPDF2
import re


class PDF():
    def __init__(self, path_file):
        self.path_file = path_file

    # Encotra o indíce uma mágina através do título
    def search_index_table_by_title(self, title="Cuadro 7"):
        read_pdf = PyPDF2.PdfFileReader(self.path_file)
        # pega o numero de páginas
        number_of_pages = read_pdf.getNumPages()
        count = 0

        while count < number_of_pages:
            page = read_pdf.getPage(count)
            page_content = page.extractText()

            # faz a junção das linhas
            parsed = ''.join(page_content)
            # remove as quebras de linha
            parsed = re.sub('n', '', parsed)

            if title in parsed:
                return str(count+1)
            count += 1

        return "index não encontrado"

    # ler as tabelas de uma página do pdf, transcrevendo as tabelas para um dataframe
    def create_table(self, index, page):
        reader = PyPDF2.PdfFileReader(self.path_file)
        page_table = reader.pages[int(page)-1]
        text = page_table.extract_text()
        li = list(text.split("\n"))
        date_report = list(filter(lambda x: x.startswith("Comprende"), li))[
            0].split("al")[1]

        table_list = tabula.read_pdf(self.path_file, pages=page)
        df = table_list[index]
        header = list(df.columns)
        if index != 0:
            header[:] = [x for x in header if not x.startswith('Unnamed:')]

        df = df.rename(columns={
            header[0]: 'Ingenio',
            header[1]: 'Superficie industrializada',
            header[2]: 'Caña molida',
            header[3]: 'Rendimiento de campo',
            header[4]: 'Producción de azúcar',
            header[5]: 'Rendimiento de fábrica',
            header[6]: 'Rendimiento agroindustrial',
            header[7]: 'Azúcar refinada',
            header[8]: 'Azúcar estándar',
            header[9]: 'Azúcar blanco especial',
            header[10]: 'Azúcar mascabado',
            header[11]: 'Azúcar con pol menor a 99.2'})

        df['Data do Report'] = date_report

        if index == 2:
            df = df.drop(columns=["Unnamed: 0", "Unnamed: 1"])

        df_header = pd.DataFrame([header], columns=['Ingenio',
                                                    'Superficie industrializada',
                                                    'Caña molida',
                                                    'Rendimiento de campo',
                                                    'Producción de azúcar',
                                                    'Rendimiento de fábrica',
                                                    'Rendimiento agroindustrial',
                                                    'Azúcar refinada',
                                                    'Azúcar estándar',
                                                    'Azúcar blanco especial',
                                                    'Azúcar mascabado',
                                                    'Azúcar con pol menor a 99.2'
                                                    ])

        if index == 0:
            df = df.drop([0, 1, 2])

        if index != 0:
            df = pd.concat([df, df_header])
        # df = df.append(
        #     pd.Series(header, index=df.columns[:len(header)]), ignore_index=True)
        df = df.replace('-.1', '-', regex=True)
        df = df.where(pd.notnull(df), None)
        df = df.replace(' ', '', regex=True)
        if index != 0:
            df = df.iloc[np.arange(-1, len(df)-1)]
        df = df.reset_index(drop=True)

        df_final = df.drop(['Rendimiento de campo', 'Producción de azúcar', 'Rendimiento de fábrica', 'Rendimiento agroindustrial',
                           'Azúcar refinada', 'Azúcar estándar', 'Azúcar mascabado', 'Azúcar con pol menor a 99.2'], axis=1)

        return df_final


if __name__ == '__main__':
    ...
