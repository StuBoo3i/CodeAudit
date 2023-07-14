import re


def function_body(function_info):
    """
    重组函数体
    :param function_info: 函数信息列表
    :return: 函数体
    """

    return function_info['return_type'] + ' ' + function_info['function'] + '(' + function_info[
        'parameter'] + ')' + ' {' + '\n' + function_info['function_text'] + '\n' + '}'


def replace_comments(string):
    lines = string.split('\n')  # 按行分割字符串
    for i, line in enumerate(lines):
        if '//' in line:
            lines[i] = re.sub(r'//.*', '', line)  # 使用正则表达式替换注释部分为''
    new_string = '\n'.join(lines)  # 将处理后的行重新连接为字符串

    return new_string
