import mysql.connector
import re


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

    @staticmethod
    def insert_scan_function(cnx, cursor, data_list):
        # 使用正则表达式匹配参数
        pattern = r"\b\w+\s\w+\b"
        matches = re.findall(pattern, data_list["parameter"])

        # 将匹配到的参数存储到列表中
        param_list = list(matches)

        insert_query = "INSERT INTO scan_function ( return_type, `function`, parameter, " \
                       "  function_text, belong_file, `start`, `end`," \
                       "  parameters, function_type, risk) VALUES " \
                       "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (data_list['return_type'], data_list['function_name'], param_list, data_list['body'],
                data_list['path'], data_list['start'], data_list['end'], param_list.__len__(), '0', '0')
        cursor.execute(insert_query, data)
        # 提交
        cnx.commit()

    def select_SQL(self, cursor):
        pass

    def delete_SQL(self, cnx, cursor):

        pass

    def close_SQL(self, cursor, cnx):
        # 关闭游标对象和数据库连接
        cursor.close()
        cnx.close()
