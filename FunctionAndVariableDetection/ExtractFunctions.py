import re


def process_c_files(node, file_path):
    """
    对一个树的根节点进行检查，是否是C语言文件，并对其进行迭代循环操作
    :param node:项目根节点
    :param file_path:文件的绝对路径
    :return:custom_functions, library_functions 自定义函数名（list）,库函数名（list）
    """
    custom_functions = []
    library_functions = []

    if node is None:
        return custom_functions, library_functions

    # 传入的绝对路径生成文件路径
    file_name = file_path + '/' + node.name

    if file_name.endswith(".c"):
        with open(file_name, "r") as file:
            content = file.read()

            # 进行自定义函数和库函数的筛选
            # 这里只是示例，您需要根据具体的筛选条件进行修改
            custom_functions, library_functions = extract_functions(content)

    for child_node in node.children:
        custom, library = process_c_files(child_node, file_name)
        custom_functions.extend(custom)
        library_functions.extend(library)

    # 去重操作
    custom_functions = list(set(custom_functions))
    library_functions = list(set(library_functions))

    return custom_functions, library_functions


def extract_functions(content):
    """
    读取文件内容对函数名进行正则匹配
    :param content:从文件中读取的内容
    :return:custom_functions, library_functions 自定义函数名（list）,库函数名（list）
    """
    custom_functions = []
    library_functions = []

    pattern_custom = r'\b(?:int|void|char|short|long|float|double)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
    pattern_library = r'(?<!\w)([a-zA-Z_][a-zA-Z0-9_]*)\s*\('

    matches_custom = re.findall(pattern_custom, content)
    matches_library = re.findall(pattern_library, content)

    # 自定义中删除main
    custom_functions = [func for func in matches_custom if func != 'main']
    for func in matches_library:
        if func not in custom_functions:
            library_functions.append(func)

    # 去重操作
    custom_functions = list(set(custom_functions))
    library_functions = list(set(library_functions))

    return custom_functions, library_functions
