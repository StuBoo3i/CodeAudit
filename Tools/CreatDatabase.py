import mysql.connector
from Tools.DatabaseOperation import SQL


# 创建数据库
def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE code_audit")
        print("数据库创建成功了喵")
    except mysql.connector.Error as err:
        print("数据库创建失败了喵: {}".format(err))


# 使用新创建的数据库
def use_database(cursor):
    try:
        cursor.execute("USE code_audit")
        print("已经在使用数据库了喵")
    except mysql.connector.Error as err:
        print("切换数据库失败了喵: {}".format(err))


# 创建表
def create_table1(cursor):
    try:
        cursor.execute(
            "CREATE TABLE scan_function ("
            "id INT AUTO_INCREMENT PRIMARY KEY,"
            "`function` VARCHAR(255),"
            "function_text TEXT,"
            "return_type VARCHAR(255),"
            "parameter VARCHAR(510),"
            "parameters INT,"
            "function_type BOOL,"
            "belong_file VARCHAR(255),"
            "`start` INT,"
            "`end` INT,"
            "risk BOOL)"
        )
        print("表scan_function创建成功了喵")
    except mysql.connector.Error as err:
        print("表scan_function创建失败了喵: {}".format(err))


def create_table2(cursor):
    try:
        cursor.execute('''CREATE TABLE c_function
                                  (id INT AUTO_INCREMENT PRIMARY KEY,
                                   `function` VARCHAR(255),
                                   severity VARCHAR(255),
                                   solution VARCHAR(255))''')
        print("表c_function创建成功了喵")
    except mysql.connector.Error as err:
        print("表c_function创建失败了喵:{}".format(err))


def create_table3(cursor):
    try:
        cursor.execute('''CREATE TABLE file_relationships
                                  (id INT AUTO_INCREMENT PRIMARY KEY,
                                   `file` VARCHAR(255),
                                   include VARCHAR(255))''')
        print("表file_relationships创建成功了喵")
    except mysql.connector.Error as err:
        print("表file_relationships创建失败了喵: {}".format(err))


def create_table4(cursor):
    try:
        cursor.execute('''CREATE TABLE function_tree
                                  (id INT AUTO_INCREMENT PRIMARY KEY,
                                   function_id INT,
                                   pre_function VARCHAR(255),
                                   sub_function VARCHAR(255))''')
        print("表function_tree创建成功了喵")
    except mysql.connector.Error as err:
        print("表function_tree创建失败了喵: {}".format(err))


def create_table5(cursor):
    try:
        cursor.execute('''CREATE TABLE value_of_function
                                  (id INT AUTO_INCREMENT PRIMARY KEY,
                                   function_id INT,
                                   `values` VARCHAR(255))''')
        print("表value_of_function创建成功了喵")
    except mysql.connector.Error as err:
        print("表value_of_function创建失败了喵: {}".format(err))


def set_table():
    mysql = SQL()
    insert_query = "INSERT INTO c_function (id, `function`, severity, solution) VALUES (%s, %s, %s, %s) " \
                   "ON DUPLICATE KEY UPDATE `function` = VALUES(`function`), " \
                   "severity = VALUES(severity), solution = VALUES(solution)"
    data = (-1, "leak_function", "很危险", "确保你的函数进行了严格的内存检查")
    mysql.cursor.execute(insert_query, data)

    insert_query = "INSERT INTO c_function (id, `function`, severity, solution) VALUES (%s, %s, %s, %s) " \
                   "ON DUPLICATE KEY UPDATE `function` = VALUES(`function`), " \
                   "severity = VALUES(severity), solution = VALUES(solution)"
    data = (-2, "unused_function", "注意", "请删除无用的函数")
    mysql.cursor.execute(insert_query, data)
    # 提交
    mysql.cnx.commit()
    mysql.close_SQL(mysql.cursor, mysql.cnx)
    print("初始化表c_function完成啦，快去执行ReadTableAboutCFunction.py吧")


if __name__ == '__main__':
    # 连接到MySQL数据库
    cnx = mysql.connector.connect(user='root', password='100221', host='localhost')
    # 获取游标
    cursor = cnx.cursor()
    # 创建数据库
    create_database(cursor)
    # 使用新创建的数据库
    use_database(cursor)
    # 创建表
    create_table1(cursor)
    create_table2(cursor)
    create_table3(cursor)
    create_table4(cursor)
    create_table5(cursor)
    set_table()
    # 关闭游标和连接
    cursor.close()
    cnx.close()
