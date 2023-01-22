import pandas as pd
import tabula
import numpy as np


class PDF():
    def __init__(self, file_name):
        self.table_list = tabula.read_pdf(file_name, pages="6")

    def len_table_list(self):
        print(len(self.table_list))

    def create_table1(self):
        df = self.table_list[0]
        header = list(df.columns)
        df = df.rename(columns={header[0]: 'Ingenio',
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

        df = df.drop([0, 1])
        df = df.where(pd.notnull(df), None)
        df = df.replace(' ', '', regex=True)
        df = df.reset_index(drop=True)

        return df

    def create_table(self, index):
        df = self.table_list[index]
        header = list(df.columns)
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
        df = pd.concat([df, df_header])
        # df = df.append(
        #     pd.Series(header, index=df.columns[:len(header)]), ignore_index=True)
        df = df.replace('-.1', '-', regex=True)
        df = df.where(pd.notnull(df), None)
        df = df.replace(' ', '', regex=True)
        df = df.iloc[np.arange(-1, len(df)-1)]
        df = df.reset_index(drop=True)

        return df


if __name__ == '__main__':
    pdf1 = PDF("Reporte_36.pdf")
    pdf1.len_table_list()

    tb1 = pdf1.create_table1()
    tb2 = pdf1.create_table(1)
