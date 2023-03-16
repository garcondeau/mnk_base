from SupplierScripts import *


def elit_to_db():
    table_name = 'elit'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_elit_data())
    DataFrameReader.supplier_to_ftp(table_name)


def get_elit_data():
    elit = Elit()
    data = elit.process()

    query = '''
        SELECT
            19 as supplier_id,
            manufacturer,
            supplier_part_number,
            part_number,
            price,
            CAST( (REPLACE(qty_lublin, '>', '') + REPLACE(qty_wroclaw, '>', '') + 
            REPLACE(qty_cn, '>', '')) AS INTEGER) as quantity,
            tecdoc_number,
            tecdoc_supplier_number,
            ean_number
        FROM
            data
        '''

    return sqldf(query)


class Elit:
    def __init__(self):
        data_url = "ftp://elit:kI9eP6jB1v@138.201.56.185/export.csv"

        self.data_columns = {
            0: 'supplier_ad_number', 1: 'supplier_part_number', 2: 'part_name',
            3: 'price', 5: 'manufacturer', 6: 'part_number', 7: 'qty_lublin',
            8: 'qty_cn', 9: 'qty_wroclaw', 13: 'tecdoc_number',
            14: 'tecdoc_supplier_number', 17: 'ean_number'
        }

        self.data = pd.read_csv(data_url, header=None, usecols=[0, 1, 2, 3, 5, 6, 7, 8, 9, 13, 14, 17], skiprows=1,
                                sep=';', encoding_errors='ignore', engine='python', error_bad_lines=False)

    def process(self):
        self.data.rename(columns=self.data_columns, inplace=True)

        return self.data
