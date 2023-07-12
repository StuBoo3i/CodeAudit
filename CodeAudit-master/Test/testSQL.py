from Tools.DatabaseOperation import SQL
from FunctionAndVariableDetection.ExtractFunctions import function_body

if __name__ == '__main__':
    mysql = SQL()
    ss = mysql.select_scan_function(mysql.cursor)
    print(ss)
    # for s in ss:
    #     print(function_body(s))

