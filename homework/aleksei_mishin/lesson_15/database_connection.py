import mysql.connector as mysql


class MySqlConnection:

    def __init__(self, user: str, passwd: str, host: str, port: int, database: str):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.database = database
        self.db = None
        self.cursor = None

    def connect_to_db(self):
        self.db = mysql.connect(
            user=self.user,
            passwd=self.passwd,
            host=self.host,
            port=self.port,
            database=self.database
        )
        self.cursor = self.db.cursor(dictionary=True)

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()

    def __enter__(self):
        self.connect_to_db()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()
