from SupplierScripts import *


def motogama_to_db():
    table_name = 'motogama'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_motogama_data())
    DataFrameReader.supplier_to_ftp(table_name)


def get_motogama_data():
    motogama = Motogama()
    data = motogama.process()
    query = '''
        SELECT
            40 as supplier_id,
            manufacturer,
            supplier_part_number,
            part_number,
            price,
            CAST(REPLACE(qty, '> ', '') AS INTEGER) as quantity,
            pack,
            part_name
        FROM
            data
        WHERE
            CAST(REPLACE(qty, '> ', '') AS INTEGER) > 0 
    '''
    return sqldf(query)


class Motogama:
    def __init__(self):
        self.data_columns = {
            0: 'supplier_part_number', 1: 'part_name', 2: 'qty',
            3: 'price', 5: 'part_number', 7: 'manufacturer', 8: 'pack'
        }
        data_url = "ftp://motogama:hH1gJ0zK2t@138.201.56.185/19134_01.csv"
        self.data = pd.read_csv(data_url, sep=';', header=None,
                                encoding_errors='ignore', usecols=[0, 1, 2, 3, 5, 7, 8])

    def process(self):
        self.data.rename(columns=self.data_columns, inplace=True)

        return self.data
