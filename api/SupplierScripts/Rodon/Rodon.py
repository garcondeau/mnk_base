from SupplierScripts import *


def rodon_to_db():
    table_name = 'rodon'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_rodon_data())
    DataFrameReader.supplier_to_ftp(table_name)


def get_rodon_data():
    rodon = Rodon()
    dataframes = rodon.process()
    data = dataframes[0]
    dict = dataframes[1]

    query = '''
           SELECT
           60 as supplier_id,
           dict.manufacturer,
           data.supplier_part_number,
           dict.part_number,
           data.part_name,
           CAST(data.qty AS INTEGER) as quantity,
           IIF(data.deposit is not null, data.price + data.deposit, data.price) as price
           FROM data
           INNER JOIN dict
           ON data.supplier_part_number = dict.supplier_part_number
           WHERE data.qty > 0
           AND data.price > 0
           AND data.part_group not like 'WYCOFANE'
    '''

    return sqldf(query)


class Rodon:
    def __init__(self):
        self.data_columns = {
            0: 'supplier_part_number',
            2: 'part_name',
            3: 'qty',
            4: 'price',
            5: 'price_without_discount',
            7: 'part_group',
            11: 'pack',
            13: 'deposit'
        }
        self.dict_columns = {0: 'supplier_part_number', 1: 'part_number', 2: 'manufacturer'}

        data_url = "ftp://rodon:nA1cC3zC8ztV3v@138.201.56.185/57765_01.gz"
        dict_url = "ftp://rodon:nA1cC3zC8ztV3v@138.201.56.185/rodon_dict.csv"
        self.data = pd.read_csv(data_url, sep=';', low_memory=False, compression='gzip',
                           encoding_errors='ignore', header=None, usecols=[0, 2, 3, 4, 5, 7, 11, 13])

        self.dict = pd.read_csv(dict_url, header=None, low_memory=False,
                           sep='\t', encoding_errors='ignore')

    def process(self):
        self.data.rename(columns=self.data_columns, inplace=True)
        self.dict.rename(columns=self.dict_columns, inplace=True)
        return [self.data, self.dict]
