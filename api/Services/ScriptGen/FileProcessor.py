import pandas as pd


class FileProcessor:
    def __init__(self):
        pass

    def process_file(self, params, url):
        processed_file = pd.DataFrame()

        if params['file_type'] == 'csv':
            processed_file = pd.read_csv(
                url,
                encoding_errors=params['encoding_errors'],
                sep=params['sep'],
                header=params['header'],
                low_memory=params['low_memory'],
                compression=params['compression'],
                error_bad_lines=params['error_bad_lines'],
                usecols=params['use_cols'],
                skiprows=params['skip_rows'],
                engine=params['engine'],
                decimal=params['decimal'],

            )
        elif params['file_type'] == 'excel':
            processed_file = pd.read_excel(url)

        print(params['columns'])

        processed_file.rename(columns=params['columns'], inplace=True)

        print(processed_file)

        return processed_file
