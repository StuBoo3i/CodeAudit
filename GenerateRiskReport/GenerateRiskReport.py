from Tools.DatabaseOperation import SQL
from FunctionManagement import RiskFunctionManagement


def report():
    """
    调用GenerateRiskReport完成报告创建
    :return: 报告
    """
    Report = ""
    mysql = SQL()
    leaks = []
    invallids = []
    risk_functions = []
    low_risk_functions = []
    high_risk_functions = []
    medium_risk_functions = []

    RiskFunctionManagement.detect_library_function()
    RiskFunctionManagement.test_static_leak()
    RiskFunctionManagement.test_invalid_function()
    functions = mysql.select_scan_function(mysql.cursor)

    for function in functions:
        if function['risk'] != 0:
            risk_functions.append(function)

    for risk_function in risk_functions:
        if 32 <= risk_function['risk'] <= 50:
            high_risk_functions.append(risk_function)
        elif 51 <= risk_function['risk'] <= 54:
            medium_risk_functions.append(risk_function)
        elif 55 <= risk_function['risk'] <= 62:
            low_risk_functions.append(risk_function)
        elif risk_function['risk'] == -1:
            leaks.append(risk_function)
        elif risk_function['risk'] == -2:
            invallids.append(risk_function)

    # print("统计结果")
    # print("高等风险函数"+high_risk_functions.__len__() + "个\t中等风险函数" + medium_risk_functions.__len__() +
    #       "个\t低等风险函数" + low_risk_functions.__len__() + "个")
    # print("高等风险函数")
    # for high_risk_function in high_risk_functions:
    #     print("函数名:" + high_risk_function['function'] + " 位于" + high_risk_function['belong_file'] +
    #           "文件第" + high_risk_function['start'] + "行")
    # print("中等风险函数")
    # for medium_risk_function in medium_risk_functions:
    #     print("函数名:" + medium_risk_function['function'] + " 位于" + medium_risk_function['belong_file'] +
    #           "文件第" + medium_risk_function['start'] + "行")
    # print("低等风险函数")
    # for low_risk_function in low_risk_functions:
    #     print("函数名:" + low_risk_function['function'] + " 位于" + low_risk_function['belong_file'] +
    #           "文件第" + low_risk_function['start'] + "行")
    # print("内存泄漏函数")
    # for leak in leaks:
    #     print("名称:" + leak['function'] + " 位于" + leak['belong_file'] + "文件第" + leak['start'] + "行")
    # print("未被使用函数")
    # for i in invallids:
    #     print("名称:" + i['function'] + " 位于" + i['belong_file'] + "文件第" + i['start'] + "行")

    Report += "统计结果\n"
    Report += "高等风险函数"+high_risk_functions.__len__() + "个\t中等风险函数" + medium_risk_functions.__len__() + \
              "个\t低等风险函数" + low_risk_functions.__len__() + "个\n"
    Report += "高等风险函数\n"
    for high_risk_function in high_risk_functions:
        Report += "函数名:" + high_risk_function['function'] + " 位于" + high_risk_function['belong_file'] + \
                  "文件第" + high_risk_function['start'] + "行\n"
    Report += "中等风险函数\n"
    for medium_risk_function in medium_risk_functions:
        Report += "函数名:" + medium_risk_function['function'] + " 位于" + medium_risk_function['belong_file'] + \
                  "文件第" + medium_risk_function['start'] + "行\n"
    Report += "低等风险函数\n"
    for low_risk_function in low_risk_functions:
        Report += "函数名:" + low_risk_function['function'] + " 位于" + low_risk_function['belong_file'] + \
                  "文件第" + low_risk_function['start'] + "行\n"
    Report += "内存泄漏函数\n"
    for leak in leaks:
        Report += "名称:" + leak['function'] + " 位于" + leak['belong_file'] + "文件第" + leak['start'] + "行\n"
    Report += "未被使用函数\n"
    for i in invallids:
        Report += "名称:" + i['function'] + " 位于" + i['belong_file'] + "文件第" + i['start'] + "行\n"

    return Report
