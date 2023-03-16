import pandas as pd
from threading import Thread, active_count
from Services.Db.DbContext import DbContext
from Services.Db.DbService import DbService
from Utils.consts import CONSOLE_COLOR, PATHS, ERRORS
from Services.Ftp.FtpConnection import FtpConnection


def format_column(column: pd.Series):
    column = column.str.upper()
    column = column.str.replace('[\W_]+', '', regex=True)
    column = column.str.strip()
    return column


class DataFrameReader:
    @staticmethod
    def dataframe_to_db(table_name, dataframe):
        context = DbContext()
        connection = context.db
        dataframe['part_number'] = format_column(dataframe['part_number'])
        dataframe.to_sql(table_name, connection, if_exists='replace', index=False)
        DataFrameReader.supplier_to_ftp(table_name)

    @staticmethod
    def supplier_to_ftp(supplier):
        db = DbService()
        print('Exporting {} to csv'.format(supplier))
        file = db.get_table_csv(supplier)
        ftp = FtpConnection('138.201.56.185', 'ph6802', 'z7lIh8iv10pLRt')
        ftp.upload_file(file, 'maxi_export', supplier)
