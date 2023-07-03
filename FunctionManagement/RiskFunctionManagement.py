from Tools.DatabaseOperation import SQL
from LeakDetection.LeakDetection import static_position
from FunctionAndVariableDetection.ExtractFunctions import function_body
import re

def test_static_leak():
    mysql = SQL()
    results = mysql.select_file(mysql.cursor)

    for result in results:
        print(static_position(result))
        # 使用正则表达式提取文本
        # pattern = r":\d+:\d+:"
        # matches = re.findall(pattern, static_position(result))
        # print(matches)
        print(mysql.select_id_by_path(mysql.cursor, result))
