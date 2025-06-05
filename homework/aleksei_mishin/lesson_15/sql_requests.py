from homework.aleksei_mishin.lesson_15.database_connection import MySqlConnection


class SqlRequests(MySqlConnection):

    def commit_changes(self):
        self.db.commit()

    @staticmethod
    def checking_quantity_of_params(columns: (list, tuple), values: (list, tuple)):
        if len(columns) != len(values):
            raise ValueError(f"Quantity of columns and values is not equal!\n"
                             f"Columns: {columns}\n"
                             f"Values: {values}")

    def get_last_id(self) -> int:
        return self.cursor.lastrowid

    def insert_into_table(self,
                          table_name: str,
                          columns: (list, tuple),
                          values: (list, tuple)) -> int:
        params_quan = 0

        for col in values:
            params_quan = len(col)
            self.checking_quantity_of_params(columns, col)

        columns_str = ", ".join(columns)
        format_str = ", ".join(["%s"] * params_quan)
        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({format_str})"
        self.cursor.executemany(insert_query, values)

        return self.get_last_id()

    def select_from_table(self,
                          columns: str,
                          table_name: str,
                          where_columns: tuple = None,
                          where_values: tuple = None):
        alias = table_name[:3]
        if where_columns and where_values:
            self.checking_quantity_of_params(where_columns, where_values)
            columns_str = ", ".join(where_columns)
            format_str = ", ".join(["%s"] * len(where_values))
            query = f"SELECT {columns} FROM {table_name} AS {alias} WHERE ({columns_str}) = ({format_str})"
            self.cursor.execute(query, where_values)
        else:
            query = f"SELECT {columns} FROM {table_name} AS {alias}"
            self.cursor.execute(query)
        print(self.cursor.fetchall())

    def update_data_in_table(self,
                             table_name: str,
                             set_column: str,
                             set_value: (str, int, float),
                             where_column: str,
                             where_value: (str, int, float)):
        update_query = (f"UPDATE {table_name} SET {set_column} = %s "
                        f"WHERE {where_column} = %s")
        self.cursor.execute(update_query, [set_value, where_value])

        return self.get_last_id()

    def get_info_about_user(self, student_id: (str, int)):
        query = f'''
            SELECT
            name,
            second_name,
            GROUP_CONCAT(b.title) AS book_titles,
            g.title AS group_title,
            l.title AS lesson_title,
            sub.title AS subject_title,
            m.value AS mark_value
            FROM students s
            JOIN books b ON s.id = b.taken_by_student_id
            JOIN `groups` g ON s.group_id = g.id
            JOIN marks m ON s.id = m.student_id
            JOIN lessons l ON m.lesson_id = l.id
            JOIN subjets sub ON l.subject_id = sub.id
            WHERE s.id = {student_id}
            GROUP BY
            s.id, g.title, m.value, l.title, sub.title
        '''
        self.cursor.execute(query)
        print(self.cursor.fetchall())
