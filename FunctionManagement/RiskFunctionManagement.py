from Tools.DatabaseOperation import SQL
from LeakDetection.LeakDetection import static_position
from FunctionAndVariableDetection.ExtractFunctions import function_body
import re


def test_static_leak():
    mysql = SQL()
    results = mysql.select_file(mysql.cursor)

    for result in results:
        strings = static_position(result)
        for string in strings:
            # 使用正则表达式提取文本
            pattern = r":\d+:\d+:"
            # pam = "".join(result)
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
                        mysql.updata_risk_by_id(mysql.cnx, mysql.cursor, a)


def test_invalid():
    pass
