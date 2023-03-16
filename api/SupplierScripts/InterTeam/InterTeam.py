from SupplierScripts import *


def inter_team_to_db():
    table_name = 'inter_team'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_inter_team_data())
    DataFrameReader.supplier_to_ftp(table_name)


def get_inter_team_data():
    inter_team = InterTeam()
    data = inter_team.process()

    query = '''
        SELECT
            26 as supplier_id,
            manufacturer,
            part_number as supplier_part_number,
            part_number,
            price + deposit as price,
            qty_1 + qty_2 as quantity
        FROM 
            data  
    '''

    return sqldf(query)


class InterTeam:
    def __init__(self):
        self.data_columns = {
            0: 'part_number',
            1: 'part_name',
            2: 'qty_1',
            3: 'qty_2',
            4: 'price',
            5: 'manufacturer',
            6: 'deposit'
        }
        data_url = "ftp://ph6802:z7lIh8iv10pLRt@138.201.56.185/i-t/it84262.zip"
        self.data = pd.read_csv(data_url, sep=';', encoding_errors='ignore', compression='zip',
                                header=None, skiprows=1, usecols=[0, 1, 2, 3, 4, 5, 6])

    def process(self):
        self.data.rename(columns=self.data_columns, inplace=True)

        return self.data
