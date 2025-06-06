from homework.aleksei_mishin.lesson_15.database_connection import MySqlConnection


class SqlRequests(MySqlConnection):

    def commit_changes(self):
        self.db.commit()

    def get_last_id(self) -> int:
        return self.cursor.lastrowid

    def insert_or_update_data(self,
                              query: str,
                              data: (list, tuple)) -> (list, int):

        if type(data) is list and len(data) > 1:
            ids_list = []
            for v in data:
                self.cursor.execute(query, v)
                ids_list.append(self.get_last_id())
            return ids_list
        else:
            self.cursor.execute(query, data)
            return self.get_last_id()

    def get_data(self,
                 query: str,
                 data: (list, tuple)):
        self.cursor.execute(query, data)
        print(self.cursor.fetchall())
