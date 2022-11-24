from models import engine


class Connection:
    def _parse_query(self, query_dict: dict[str]):
        def rename_keys(initial_df, renamed_keys):
            return dict([(renamed_keys.get(k), v) for k, v in initial_df.items()])

        parse_keys = rename_keys(
            query_dict,
            {
                "select": "select",
                "where": "where",
                "group_by": "group by",
                "order_by": "order by",
                "sort_by": "sort by",
            },
        )

        clean_query = {
            key: value for key, value in parse_keys.items() if value is not None
        }

        sql_statement = ""
        for key, value in clean_query.items():
            sql_statement += key + " " + value
            sql_statement += " "
            if key == "select":
                sql_statement += "from analytics "

        sql_statement += ";"
        return sql_statement

    def _run_query(self, query):
        with engine.connect() as connection:
            result = connection.execute(query)
        return result.fetchall()

    def request_query(self, query_dict: dict[str]):
        parsed_query = self._parse_query(query_dict)
        data = self._run_query(parsed_query)
        return data
