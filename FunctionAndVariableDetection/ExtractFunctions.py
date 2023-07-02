import re


def process_c_files(node, file_path):
    """
    对一个树的根节点进行检查，是否是C语言文件，并对其进行迭代循环操作
    :param node:项目根节点
    :param file_path:文件的绝对路径
    :return:custom_functions, library_functions 自定义函数名（list）,库函数名（list）
    """
    functions = []

    if node is None:
        return functions

    # 传入的绝对路径生成文件路径
    file_name = file_path + '/' + node.name

    if file_name.endswith(".c"):
        with open(file_name, "r") as file:
            content = file.read()

            # 进行函数的筛选与处理
            functions = extract_functions(content, file_name)

    for node_child in node.children:
        functions_child = process_c_files(node_child, file_name)
        functions.extend(functions_child)

    return functions


def extract_functions(content, path):
    """
    读取文件内容对函数进行正则匹配，并提取返回类型、函数名、参数列表和函数体
    :param path: 文件所在的绝对路径
    :param content: 从文件中读取的内容
    :return: functions 函数信息（list），每个元素是一个字典包含返回类型、函数名、参数列表和函数体
    """
    functions = []

    pattern_definition = r'((?:int|void|char|short|long|float|double)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(([^)]*)\)\s*{([' \
                         r'^}]*)})'

    matches_definition = re.findall(pattern_definition, content)

    for definition in matches_definition:
        return_type, function_name, params, body = definition
        return_type = return_type.split()[0]  # 提取返回类型的第一个单词
        start_line, end_line = find_func_body_lines(content, '{' + body + '}')
        function_info = {
            'return_type': return_type.strip(),
            'function_name': function_name.strip(),
            'parameters': params.strip(),
            'body': body.strip(),
            'path': path,
            'start': start_line,
            'end': end_line
        }
        functions.append(function_info)

    return functions


def find_func_body_lines(content, func_body):
    """
    查找函数主体在内容中的起止行数
    :param content: 完整内容字符串
    :param func_body: 函数主体字符串
    :return: 起始行号，结束行号
    """
    pattern = r"(?<!\w)" + re.escape(func_body.strip()) + r"(?!\w)"
    match = re.search(pattern, content)
    if match:
        start_line = content.count('\n', 0, match.start()) + 1
        end_line = content.count('\n', 0, match.end())
        return start_line, end_line

    return -1, -1
