from SupplierScripts import *


def autoland_to_db():
    table_name = 'autoland'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_autoland_data())


def get_autoland_data():
    autoland = AutoLand()
    data = autoland.process()

    query = '''
        SELECT
            5 as supplier_id,
            manufacturer,
            supplier_part_number,
            part_number,
            CAST(REPLACE(qty, '>', '') AS INTEGER) as quantity,
            IIF(deposit is null, price, deposit + price) as price,
            pack
        FROM
            data
        WHERE
            part_number is not null
    '''

    return sqldf(query)

class AutoLand:
    def __init__(self):
        data_url = "ftp://ph6802:z7lIh8iv10pLRt@138.201.56.185/autolend/156127_w2.zip"

        self.data_columns = {
            0: 'supplier_part_number',
            1: 'part_name',
            2: 'qty',
            3: 'price',
            4: 'part_number',
            6: 'manufacturer',
            7: 'pack',
            9: 'deposit'
        }

        self.data = pd.read_csv(data_url, compression='zip', sep=';', encoding_errors='ignore', header=None,
                                low_memory=False, usecols=[0, 1, 2, 3, 4, 6, 7, 9])

    def process(self):
        self.data.rename(columns=self.data_columns, inplace=True)

        return self.data