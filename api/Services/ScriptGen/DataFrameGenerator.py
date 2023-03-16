import pandas as pd
from Services.ScriptGen.ParamsBuilder import ParamsBuilder
from Services.ScriptGen.SQLGen import SQLGen
from Services.load_config import Config


class DataFrameGenerator:
    @classmethod
    def get_supplier_dataframe(cls, params):
        supplier_name = params['supplier_name']
        print(f'Getting {supplier_name} data frames')
        files = params['files']
        dfs = []
        for file_params in files:
            df = DataFrameGenerator.get_dataframe(file_params)
            df.set_index('supplier_part_number')
            dfs.append(df)
        pd.set_option('display.max_columns', 100)
        df = pd.concat([df for df in dfs], ignore_index=False, axis=1)
        df = df.loc[:, ~df.columns.duplicated()]
        return df

    @classmethod
    def get_dataframe(cls, params):
        print(f"\tFile: {params['file_name']}")
        print(params)
        if 'csv' in params['file_type']:
            print('reading as csv')
            df = pd.read_csv(
                filepath_or_buffer=params['filepath_or_buffer'],
                sep=params['sep'],
                decimal=params['decimal'],
                skiprows=params['skip_rows'],
                header=params['header'],
                compression=params['compression'],
                low_memory=params['low_memory'],
                encoding_errors=params['encoding_errors'],
                encoding=params['encoding'],
                engine=params['engine'],
                on_bad_lines=params['on_bad_lines'],
                usecols=params['use_cols'],
            )
            return df.rename(columns=params['columns'])
        elif 'excel' in params['file_type']:
            print('reading as excel')
            return pd.read_excel(
                io=params['filepath_or_buffer'],
                decimal=params['decimal'],
                header=params['header'],
                skiprows=params['skip_rows']
            )
        else:
            return

    @staticmethod
    def process_suppliers_from_config(config = Config()):
        suppliers = config.get_app_suppliers()
        for supplier_params in suppliers:
            params = ParamsBuilder.get_supplier_params(supplier_params)
            if params['status']:
                print(params)
                df = DataFrameGenerator.get_supplier_dataframe(params)
                df = SQLGen.get_queried_data(df, params)
                print(df)
            else:
                print(f'Supplier {params["supplier_name"]} is disabled')
