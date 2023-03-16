from SupplierScripts import *


def paketo_to_db():
    table_name = 'paketo'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_paketo_data())
    DataFrameReader.supplier_to_ftp(table_name)


def get_paketo_data():
    paketo = Paketo()
    data = paketo.process()
    query = '''
        SELECT 
        48 as supplier_id,
        "FEBEST" as manufacturer,
        data.supplier_part_number,
        data.part_number, 
        data.price,  
        CAST(data.qty AS INT) AS quantity
        FROM data
        WHERE data.qty NOT LIKE '0.0' AND data.price NOT LIKE '0.0'
    '''
    return sqldf(query)


class Paketo:
    def __init__(self):
        self.data_columns = {0: 'part_number', 1: 'price', 2: 'currency', 3: 'qty'}

        data_url = 'ftp://paketo:yX5iS0yF2jrO0l@138.201.56.185/CENNIK PAKETO.csv'
        self.data = pd.read_csv(data_url, encoding_errors='ignore', sep=';', header=None, skiprows=1)

    def process(self):
        self.data.drop(self.data.columns[[4]], axis=1, inplace=True)
        self.data.rename(columns=self.data_columns, inplace=True)
        self.data['supplier_part_number'] = self.data['part_number']
        self.data.set_index('part_number', inplace=True)
        self.data.columns = self.data.columns.str.strip()
        return self.data
