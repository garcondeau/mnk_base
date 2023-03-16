import pandas as pd
from pandasql import sqldf

data_url = "ftp://plichta:zL1lS3cH6o@138.201.56.185/plichta_data.csv"
dict_url = "ftp://plichta:zL1lS3cH6o@138.201.56.185/plichta_dict.csv"

data = pd.read_csv(data_url, sep='\t', header=None, skiprows=1, encoding_errors='ignore', low_memory=False, usecols=[0, 1, 8], decimal=',')
dict = pd.read_csv(dict_url, sep=';', header=None, skiprows=1, encoding_errors='ignore', low_memory=False, usecols=[0])
data_columns = {
    0: 'part_number',
    1: 'part_name',
    8: 'price'
}

dict_columns = {
    0: 'part_number'
}

data.rename(columns=data_columns, inplace=True)
dict.rename(columns=dict_columns, inplace=True)

query = '''
    SELECT
        49 as supplier_id,
        "VAG" as manufacturer,
        data.part_name,
        data.part_number as supplier_part_number,
        data.part_number,
        data.price,
        999 as quantity
    FROM
        data
    INNER JOIN
        dict
    ON 
        data.part_number = dict.part_number
    WHERE
        data.price is not null

'''

sqldf(query).to_csv('D:\Work\export.csv', sep=';')