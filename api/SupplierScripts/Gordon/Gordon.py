from SupplierScripts import *


def gordon_to_db():
    table_name = 'gordon'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_gordon_data())
    DataFrameReader.supplier_to_ftp(table_name)


def get_gordon_data():
    gordon = Gordon()
    dataframes = gordon.process()
    data = dataframes[0]
    dict = dataframes[1]

    query = '''
        SELECT 
            22 as supplier_id,
            data.manufacturer,
            dict.supplier_part_number,
            dict.part_number,
            data.price,
            CAST(data.qty1 + data.qty2 AS INTEGER) as quantity,
            data.tecdoc_number_1,
            data.tecdoc_number_2
        FROM 
            dict
        INNER JOIN 
            data
        ON 
            dict.supplier_part_number = data.supplier_part_number
        WHERE 
            CAST(data.qty1 + data.qty2 AS INTEGER) > 0
        AND
            data.manufacturer is not null
        '''

    return sqldf(query)


class Gordon:
    def __init__(self):
        data_url = "ftp://gordon:tR1sG6aG7lnW5n@138.201.56.185/288090.csv"
        dict_url = "ftp://gordon:tR1sG6aG7lnW5n@138.201.56.185/gordon_dict.csv"

        self.dict_columns = {0: 'supplier_part_number', 1: 'sufix', 2: 'part_number', 3: 'manufacturer'}
        self.data_columns = {0: 'supplier_part_number', 1: 'part_name', 2: 'tecdoc_number_1', 3: 'manufacturer', 4: 'price', 5: 'tecdoc_number_2', 6: 'qty1', 7: 'qty2', 8: 'idsafo'}

        self.dict = pd.read_csv(dict_url, sep='\t', decimal=',', header=None, skiprows=2, encoding_errors='ignore', low_memory=False)
        self.data = pd.read_csv(data_url, sep='\t', decimal=',', header=None, skiprows=1, encoding_errors='ignore', low_memory=False)

    def process(self):
        self.dict.rename(columns=self.dict_columns, inplace=True)
        self.data.rename(columns=self.data_columns, inplace=True)

        return [self.data, self.dict]
