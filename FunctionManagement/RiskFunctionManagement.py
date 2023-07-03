import re
from Tools.DatabaseOperation import SQL
from LeakDetection.LeakDetection import static_position
from InvalidDetection.InvalidDetection import function_position


def test_static_leak():
    mysql = SQL()
    results = mysql.select_file(mysql.cursor)

    for result in results:
        strings = static_position(result)
        for string in strings:
            # 使用正则表达式提取文本
            pattern = r":\d+:\d+:"
            matches = re.findall(pattern, string)
            # 提取第一个数字
            if matches:
                first_match = matches[0]
                digit_pattern = r"\d+"
                digits = re.findall(digit_pattern, first_match)
                if digits:
                    ids = mysql.select_id_by_end(mysql.cursor, digits[0])
                    for i in ids:
                        a = i[0]
                        mysql.update_leak_by_id(mysql.cnx, mysql.cursor, a)

    mysql.close_SQL(mysql.cursor, mysql.cnx)


def test_invalid_function():
    mysql = SQL()
    results = mysql.select_file(mysql.cursor)

    for result in results:
        strings = function_position(result)
        for string in strings:
            # 使用正则表达式提取文本
            pattern = r":\d+:\d+:"
            matches = re.findall(pattern, string)
            # 提取第一个数字
            if matches:
                first_match = matches[0]
                digit_pattern = r"\d+"
                digits = re.findall(digit_pattern, first_match)
                if digits:
                    ids = mysql.select_id_by_start(mysql.cursor, digits[0])
                    for i in ids:
                        a = i[0]
                        mysql.update_invalid_by_id(mysql.cnx, mysql.cursor, a)

    mysql.close_SQL(mysql.cursor, mysql.cnx)


def detect_library_function():
    mysql = SQL()
    c_functions = mysql.read_function_from_c(mysql.cursor)
    s_functions = mysql.read_function_from_s(mysql.cursor)

    for s_function in s_functions:
        for c_function in c_functions:
            if s_function[1] == c_function[1]:
                mysql.update_risk_by_c(mysql.cnx, mysql.cursor, s_function[0], c_function[0])

    mysql.close_SQL(mysql.cursor, mysql.cnx)


def add_library_function(text):
    try:
        function, severity, solution = text.split(' ')
        mysql = SQL()
        # 插入数据
        insert_query = "INSERT INTO c_function (`function`, severity, solution) VALUES (%s, %s, %s)"
        mysql.cursor.execute(insert_query, (function, severity, solution))
        mysql.cnx.commit()
        mysql.close_SQL(mysql.cursor, mysql.cnx)
    except Exception as e:
        print("怎么想都插不进去吧喵（哭泣）")
        return e
