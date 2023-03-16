from SupplierScripts import *
import os
import pandas as pd
from pandasql import sqldf

def emoto_to_db():
    table_name = 'emoto'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_emoto_data())
    DataFrameReader.supplier_to_ftp(table_name)


def get_emoto_data():
    emoto = Emoto()
    dataframes = emoto.process()
    data = dataframes[0]
    dict = dataframes[1]
    part_numbers = dataframes[2]
    query = '''
        SELECT 
            17 as supplier_id,
            dict.brand AS manufacturer,
            part_numbers.supplier_part_number,
            data.part_number,
            data.part_name,  
            data.price, 
            CAST(data.qty AS INTEGER) as quantity
        FROM 
            data
        INNER JOIN 
            dict
        ON 
            dict.manufacturer = data.manufacturer
        INNER JOIN 
            part_numbers
        ON 
            part_numbers.part_number = data.part_number
        WHERE 
            qty NOT LIKE '0'
    '''
    return sqldf(query)


class Emoto:
    pd.set_option('display.max_columns', 999)

    def __init__(self):
        data_url = 'ftp://ph6802:z7lIh8iv10pLRt@138.201.56.185/e-moto/STANY54672.zip'
        dict_url = 'ftp://ph6802:z7lIh8iv10pLRt@138.201.56.185/e-moto/emoto_dict.csv'

        self.data_columns = {0: 'part_number', 1: 'part_name', 2: 'price', 3: 'qty', 4: 'part_desc', 5: 'manufacturer'}
        self.dict_columns = {1: 'manufacturer', 2: 'prefix', 3: 'brand'}
        self.part_numbers_columns = {0: 'supplier_part_number', 1: 'part_number'}

        self.part_numbers = 'emoto_dict.txt'

        self.data = pd.read_csv(data_url, encoding_errors='ignore', sep=';', decimal=',', header=None, skiprows=1, compression='zip')
        self.dict = pd.read_csv(dict_url, sep=';', header=None, skiprows=1)

        with open(self.part_numbers, 'w') as fp:
            for item in self.data[0]:
                fp.write("%s;\n" % item)

    def process(self):
        self.data.rename(columns=self.data_columns, inplace=True)
        self.data.replace('>', '', regex=True, inplace=True)
        self.data.replace('.00', '', regex=True, inplace=True)

        self.dict.rename(columns=self.dict_columns, inplace=True)
        self.dict.drop(self.dict.columns[[0]], axis=1, inplace=True)

        prefix_list = self.dict['prefix']
        for item in prefix_list:
            regex = r'^(' + item + ')'
            self.data['part_number'].replace(regex, '', regex=True, inplace=True)
        part_numbers = pd.read_csv(self.part_numbers, sep=';', header=None)
        part_numbers[1] = self.data['part_number']
        part_numbers.rename(columns=self.part_numbers_columns, inplace=True)
        os.remove(self.part_numbers)

        return [self.data, self.dict, part_numbers]