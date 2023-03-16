from pandasql import sqldf


class SQLGen:
    @classmethod
    def get_query(cls, params):
        new_line = '\n'
        print('sql gen get query\nparams')
        print(params)
        sql_params = params['sql']
        sql_select = sql_params['select']
        sql_select['quantity'] = f'REPLACE(REPLACE({sql_select["quantity"]}, " ", ""), ">", "")'

        query = f'SELECT {", ".join(f"{new_line}{value} AS {key}" for key, value in sql_select.items())}' \
                f'{new_line}FROM{new_line}dataframe{new_line}'

        if 'where' in sql_params:
            sql_where = sql_params['where']
            for value, key in sql_select.items():
                sql_where = sql_where.replace(value, key)
            query = f'{query}WHERE{new_line}{sql_where}'

        print(query)
        return query

    @staticmethod
    def get_queried_data(dataframe, sql_params):
        query = SQLGen.get_query(sql_params)
        return sqldf(query)
