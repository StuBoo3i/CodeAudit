import mysql.connector


class SQL:
    """
    创建示例后记得关闭游标，调用close_SQL实现
    """
    def __init__(self):
        self.cnx = self.__connectSQL__()
        self.cursor = self.cnx.cursor()

    def __connect_SQL__(self):
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="100221",
            database="code_audit"
        )
        return cnx

    def insert_SQL(self, cnx, cursor, data_list):
        pass

    def select_SQL(self, cursor):
        pass

    def delete_SQL(self, cnx, cursor):

        pass

    def close_SQL(self, cursor, cnx):
        # 关闭游标对象和数据库连接
        cursor.close()
        cnx.close()
