import os

from SupplierScripts import *
from zipfile import ZipFile
import shutil
import urllib.request
from contextlib import closing

def hart_to_db():
    table_name = 'hart'
    print('Pushing {} to Data Base'.format(table_name))
    DataFrameReader.dataframe_to_db(table_name, get_hart_data())
    DataFrameReader.supplier_to_ftp(table_name)


def get_hart_data():
    hart = Hart()
    dataframes = hart.process()
    data = dataframes[0]
    cn = dataframes[1]
    cross = dataframes[2]
    deposit = dataframes[3]
    prices = dataframes[4]
    quantity = dataframes[5]
    weight = dataframes[6]

    query = '''
            SELECT DISTINCT
                24 AS supplier_id,
                data.manufacturer,
                data.hart_part_number as supplier_part_number, 
                data.part_number,
                data.part_name, 
                REPLACE(quantity.qty, '>', '') AS quantity, 
                IIF(deposit.price is null, prices.price, prices.price + ROUND(deposit.price, 2)) AS price,
                data.unit_measure,
                weight.weight,
                data.origin
            FROM 
                data 
            INNER JOIN prices 
                ON data.hart_part_number = prices.hart_part_number
            INNER JOIN quantity 
                ON data.hart_part_number = quantity.hart_part_number
            LEFT JOIN deposit
                ON data.hart_part_number = deposit.hart_part_number
            INNER JOIN weight
                ON data.hart_part_number = weight.hart_part_number
            WHERE
                quantity.warehouse in('V', 'S', '1') 
            '''

    return sqldf(query)


class Hart:

    def __init__(self):
        data_url = "ftp://hart:2Y1r7D0g@138.201.56.185/96285_kth.zip"
        cn_url = "ftp://hart:2Y1r7D0g@138.201.56.185/96285_CN.zip"
        cross_url = "ftp://hart:2Y1r7D0g@138.201.56.185/96285_cross.zip"
        deposit_url = "ftp://hart:2Y1r7D0g@138.201.56.185/96285_kz.zip"
        price_qty_url = "ftp://hart:2Y1r7D0g@138.201.56.185/hart.zip"
        weight_url = "ftp://hart:2Y1r7D0g@138.201.56.185/96285_kth+wgh.zip"

        price_qty_tmp_path = 'SupplierScripts/Hart/price_qty_data.zip'

        with closing(urllib.request.urlopen(price_qty_url)) as r:
            with open(price_qty_tmp_path, 'wb') as f:
                shutil.copyfileobj(r, f)
        price_qty_zip = ZipFile(price_qty_tmp_path)

        self.data = pd.read_csv(data_url, sep=';', header=None, skiprows=1, decimal=',', usecols=[0, 1, 2, 3, 4, 6, 11, 12], compression='zip')
        self.cn = pd.read_csv(cn_url, sep=';', header=None, skiprows=1, decimal=',', usecols=[0, 1], compression='zip')
        self.cross = pd.read_csv(cross_url, sep=';', header=None, skiprows=1, decimal=',', usecols=[0, 4, 5, 6, 7], compression='zip')
        self.deposit = pd.read_csv(deposit_url, sep=';', header=None, skiprows=1, decimal=',', usecols=[0, 2], compression='zip')
        self.prices = pd.read_csv(price_qty_zip.open('96285_PriceList_PLN.csv'), sep=';', header=None, skiprows=1, decimal=',')
        self.quantity = pd.read_csv(price_qty_zip.open('96285_Quantity.csv'), sep=';', header=None, decimal=',')
        self.weight = pd.read_csv(weight_url, sep=';', header=None, skiprows=1, decimal=',', usecols=[0, 13], compression='zip')

        if os.path.exists(price_qty_tmp_path):
            os.remove(price_qty_tmp_path)

        self.quantity_columns = {0: 'hart_part_number', 1: 'qty', 2: 'warehouse'}
        self.cn_columns = {0: 'hart_part_number', 1: 'tariff_code'}
        self.deposit_columns = {0: 'hart_part_number', 2: 'price'}
        self.prices_columns = {0: 'hart_part_number', 1: 'price'}
        self.weight_columns = {0: 'hart_part_number', 13: 'weight'}
        self.data_columns = {0: 'hart_part_number', 1: 'tecdoc_number', 2: 'manufacturer', 3: 'part_number', 4: 'part_name', 6: 'unit_measure', 11: 'ean_codes', 12: 'origin'}
        self.cross_columns = {0: 'hart_part_number', 4: 'hart_part_number_cross', 5: 'part_number_cross', 6: 'part_name_cross', 7: 'manufacturer_cross'}

    def process(self):
        self.data.rename(columns=self.data_columns, inplace=True)
        self.cn.rename(columns=self.cn_columns, inplace=True)
        self.cross.rename(columns=self.cross_columns, inplace=True)
        self.deposit.rename(columns=self.deposit_columns, inplace=True)
        self.prices.rename(columns=self.prices_columns, inplace=True)
        self.quantity.rename(columns=self.quantity_columns, inplace=True)
        self.weight.rename(columns=self.weight_columns, inplace=True)

        return [self.data, self.cn, self.cross, self.deposit, self.prices, self.quantity, self.weight]
