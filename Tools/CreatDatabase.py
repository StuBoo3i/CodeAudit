import mysql.connector


# 创建数据库
def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE code_audit")
        print("数据库创建成功！")
    except mysql.connector.Error as err:
        print("数据库创建失败: {}".format(err))


# 使用新创建的数据库
def use_database(cursor):
    try:
        cursor.execute("USE code_audit")
        print("正在使用数据库！")
    except mysql.connector.Error as err:
        print("切换数据库失败: {}".format(err))


# 创建表
def create_table1(cursor):
    try:
        cursor.execute(
            "CREATE TABLE scanned_function (id INT AUTO_INCREMENT PRIMARY KEY,  `function` VARCHAR(255), "
            "`type` VARCHAR(255))")
        print("表1创建成功！")
    except mysql.connector.Error as err:
        print("表1创建失败: {}".format(err))
def create_table2(cursor):
    try:
        cursor.execute('''CREATE TABLE c_function
                                  (id INT AUTO_INCREMENT PRIMARY KEY,
                                   `function` VARCHAR(255),
                                   severity VARCHAR(255),
                                   solution VARCHAR(255))''')
        print("表2创建成功！")
    except mysql.connector.Error as err:
        print("表2创建失败: {}".format(err))

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
    # 关闭游标和连接
    cursor.close()
    cnx.close()
