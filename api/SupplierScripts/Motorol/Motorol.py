from SupplierScripts import *


def motorol_to_db():
    table_name = 'motorol'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_motorol_data())
    DataFrameReader.supplier_to_ftp(table_name)

def get_motorol_data():
    motorol = Motorol()
    dataframes = motorol.process()
    data = dataframes[0]
    dict = dataframes[1]

    query = '''
        SELECT
        42 as supplier_id,
        data.manufacturer,
        data.supplier_part_number,
        data.part_number,
        data.part_name,
        IIF(dict.deposit is not null, data.price + dict.deposit, data.price) as price,
        data.qty as quantity
        FROM data
        LEFT JOIN dict
        ON data.supplier_part_number = dict.supplier_part_number
        WHERE
        IIF(dict.deposit is not null, data.price + dict.deposit, data.price) is not null
        AND
        data.qty > 0
    '''

    return sqldf(query)


class Motorol:

    def __init__(self):
        self.data_columns = {0: 'supplier_part_number', 1: 'part_number', 2: 'part_name',
                             3: 'manufacturer', 4: 'qty', 5: 'price'}
        self.dict_columns = {0: 'supplier_part_number',
                             1: 'part_number', 2: 'manufacturer', 3: 'deposit'}

        data_url = "ftp://motorol:dE4wO8nG8o@138.201.56.185/08525.mnk.cennik.zip"
        dict_url = "ftp://motorol:dE4wO8nG8o@138.201.56.185/motorol_dict.csv"
        self.data = pd.read_csv(data_url, sep='\t', decimal=',',
                                header=None, encoding_errors='ignore', compression='zip')
        self.dict = pd.read_csv(dict_url, sep='\t', decimal=',',
                                header=None, skiprows=1, encoding_errors='ignore')

    def process(self):
        self.data.rename(columns=self.data_columns, inplace=True)
        self.dict.rename(columns=self.dict_columns, inplace=True)

        return [self.data, self.dict]
