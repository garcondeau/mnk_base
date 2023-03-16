from SupplierScripts import *


def krisauto_to_db():
    table_name = 'krisauto'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_krisauto_data())
    DataFrameReader.supplier_to_ftp(table_name)


def get_krisauto_data():
    krisauto = KrisAuto()
    dataframes = krisauto.process()
    data = dataframes[0]
    dict = dataframes[1]

    query = '''
        SELECT
            0 as supplier_id,
            data.manufacturer,
            data.supplier_part_number,
            dict.part_number,
            data.price,
            CAST(data.qty_1 + data.qty_2 + data.qty_3 AS INTEGER) as quantity
        FROM
            data    
        INNER JOIN
            dict
        ON
            data.supplier_part_number = dict.supplier_part_number
    '''

    return sqldf(query)


class KrisAuto:
    def __init__(self):
        self.data_columns = {
            0: 'supplier_part_number',
            1: 'manufacturer',
            3: 'price',
            4: 'qty_1',
            5: 'qty_2',
            9: 'qty_3'
        }
        self.dict_columns = {
            0: 'supplier_part_number',
            1: 'part_number',
            2: 'manufacturer'
        }
        data_url = "http://sklep.krisauto.pl/export/MNK_pln.zip"
        dict_url = "ftp://kris_auto:lO6fD0tH1mzP0x@138.201.56.185/krisauto_dict.csv"
        self.data = pd.read_csv(data_url, compression='zip', sep='\t', encoding_errors='ignore',
                                header=None, usecols=[0, 1, 3, 4, 5, 9])
        self.dict = pd.read_csv(dict_url, sep='\t', encoding_errors='ignore', header=None)

    def process(self):
        self.data.rename(columns=self.data_columns, inplace='True')
        self.dict.rename(columns=self.dict_columns, inplace='True')

        return [self.data, self.dict]