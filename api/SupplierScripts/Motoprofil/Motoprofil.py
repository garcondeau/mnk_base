from SupplierScripts import *


def motoprofil_to_db():
    table_name = 'motoprofil'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_motoprofil_data())
    DataFrameReader.supplier_to_ftp(table_name)


def get_motoprofil_data():
    motoprofil = Motoprofil()
    data = motoprofil.process()

    query = '''
        SELECT
            39 as supplier_id,
            manufacturer,
            part_name,
            prefix || "|" || part_number as supplier_part_number,
            part_number,
            IIF(deposit is not null, price + deposit, price) as price,
            qty as quantity,
            ean_number,
            weight
        FROM
            data
    '''

    return sqldf(query)


class Motoprofil:
    def __init__(self):
        self.data_columns = {
            0: 'prefix',
            1: 'part_number',
            2: 'manufacturer',
            3: 'part_name',
            4: 'price',
            8: 'qty',
            9: 'ean_number',
            10: 'weight',
            11: 'deposit'
        }
        data_url = "ftp://motoprofil:hF3uE4pI3fyB2v@138.201.56.185/motoprofilprice.csv"
        self.data = pd.read_csv(data_url, sep=';', encoding_errors='ignore', header=None,
                                usecols=[0, 1, 2, 3, 4, 8, 9, 10, 11], decimal=',', skiprows=1)

    def process(self):
        self.data.rename(columns=self.data_columns, inplace=True)

        return self.data
