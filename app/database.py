import pymysql

class Database:
    @staticmethod
    def get_connection():
        connection = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",
            database="djib",
        )
        return connection
