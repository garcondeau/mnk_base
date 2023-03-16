from SupplierScripts import *



def autopartner_gdansk_to_db():
    table_name = 'auto_partner_gdansk'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_autopartner_gdansk_data())
    DataFrameReader.supplier_to_ftp(table_name)

def get_autopartner_gdansk_data():
    autopartner_gdansk = AutopartnerGdansk()
    dataframes = autopartner_gdansk.process()
    data = dataframes[0]
    dict = dataframes[1]
    query = '''
        SELECT 
            7 as supplier_id,
            dict.manufacturer,
            data.supplier_part_number,
            dict.part_number, 
            data.part_name, 
            data.price,
            CAST(REPLACE(REPLACE(data.qty, '-', '0'), '> ', '') AS INTEGER) AS quantity
        FROM 
            data
        INNER JOIN 
            dict
        ON 
            dict.supplier_part_number = data.supplier_part_number
        WHERE 
            qty NOT LIKE '0'
    '''
    return sqldf(query)


class AutopartnerGdansk:
    def __init__(self):
        data_url = "ftp://autopartner_gdansk:rH4vY3yZ9iwE5a@138.201.56.185/29366_ce.gz"
        dict_url = "ftp://autopartner_gdansk:rH4vY3yZ9iwE5a@138.201.56.185/autopartner_gdansk_dict.csv"

        self.data_columns = {0: 'manufacturer', 1: 'part_name', 2: 'supplier_part_number', 3: 'qty', 4: 'price', 6: 'part_number'}
        self.dict_columns = {0: 'supplier_part_number', 1: 'part_number', 2: 'manufacturer', 3: 'part_name'}

        self.data = pd.read_csv(data_url, encoding_errors='ignore', sep=';', header=None, low_memory=False, compression='gzip')
        self.dict = pd.read_csv(dict_url, encoding_errors='ignore', sep='\t', header=None, skiprows=1)

    def process(self):
        self.data.drop(self.data.columns[[5, 7, 8]], axis=1, inplace=True)
        self.data.rename(columns=self.data_columns, inplace=True)
        self.data.set_index('part_number', inplace=True)

        self.dict.rename(columns=self.dict_columns, inplace=True)
        self.dict.set_index('part_number', inplace=True)
        return [self.data, self.dict]
