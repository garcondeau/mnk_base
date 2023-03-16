import os
import pandas as pd
from Services.Db.DbContext import DbContext

class DbService:
    @staticmethod
    def execute(query):
        context = DbContext()

        context.cursor.execute(query)
        context.db.commit()
        context.db.close()

    @staticmethod
    def select(query):
        context = DbContext()

        context.cursor.execute(query)
        result = context.cursor.fetchall()

        return result

    @staticmethod
    def get_table_csv(table_name):
        context = DbContext()
        connection = context.db
        supplier_folder = table_name.upper()
        path = os.path.join('../TemporaryStorage', supplier_folder, 'export')
        out_file_path = os.path.join(path, 'export.csv')
        if not os.path.exists(path):
            os.makedirs(path)

        table_df = pd.read_sql_query('SELECT manufacturer, supplier_part_number, '
                                     'part_number, CAST(quantity AS INTEGER) as quantity, '
                                     'ROUND(price, 2) as price FROM {} '
                                     'WHERE quantity > 0 AND price > 0'.format(table_name),
                                     connection)
        table_df.to_csv(out_file_path, sep=';', index=False)

        return out_file_path

