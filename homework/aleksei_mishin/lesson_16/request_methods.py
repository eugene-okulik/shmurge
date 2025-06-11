from homework.aleksei_mishin.lesson_16.database_connection import MySqlConnection


class SqlRequests(MySqlConnection):

    def print_if_data_not_in_db(self,
                                query: str,
                                data: list):
        for d in data:
            self.cursor.execute(query, tuple(d.values()))
            if not self.cursor.fetchone():
                print(d)
