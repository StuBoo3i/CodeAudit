import re


def generate_predecessors(successors):
    """
    根据后继函数表生成前驱函数表
    Args:successors (dict): 后继函数表，以函数ID为键，后驱函数ID列表为值
    Returns:dict: 前驱函数表，以函数ID为键，前驱函数ID列表为值
    """
    predecessors = {}

    # 遍历successors表中的每个键值对
    for function_id, successors_list in successors.items():
        # 遍历后继函数列表
        for successor_id in successors_list:
            # 如果后继函数已经在predecessors表中，则将函数ID添加到其前驱函数列表中
            if successor_id in predecessors:
                predecessors[successor_id].append(function_id)
            # 如果后继函数不在predecessors表中，则创建新的前驱函数列表
            else:
                predecessors[successor_id] = [function_id]

    return predecessors


def match_function_calls(function_info, function_call):
    """
    判断函数调用是否匹配给定的函数信息
    :param function_info: 函数信息字典
    :param function_call: 函数调用信息列表，每个元素包含函数名和参数
    :return: True（匹配）或 False（不匹配）
    """
    function_name = function_info['function_name']
    parameter_list = function_info['parameter']

    if function_call[0] == function_name:
        arguments = function_call[1]
        if check_arguments_match(arguments, parameter_list):
            return True

    return False


def check_arguments_match(arguments, parameter_list):
    """
    检查实际参数列表是否与期望参数列表模糊匹配
    :param arguments: 实际参数列表字符串
    :param parameter_list: 期望参数列表字符串
    :return: True（匹配）或 False（不匹配）
    """
    # 将参数列表字符串拆分为参数名列表
    expected_params = re.findall(r'\b[^,]+', parameter_list)

    # 将实际参数列表字符串拆分为参数值列表
    actual_values = re.findall(r'\b[^,]+', arguments)

    # 检查实际参数数量是否与期望参数数量一致
    if len(actual_values) != len(expected_params):
        return False
    return True


def extract_function_calls(code):
    """
    从代码中提取函数调用的函数名和参数
    :param code: 代码字符串
    :return: 函数调用信息的列表，每个元素包含函数名和参数
    """
    pattern = r'([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*?)\)'
    matches = re.findall(pattern, code)
    function_calls = [(match[0], match[1]) for match in matches]
    return function_calls


if __name__ == '__main__':
    function_info = {'return_type': 'int', 'function_name': 'add', 'parameter': 'int a, int b', 'body': 'c = a + b - '
                                                                                                        '1;\n    '
                                                                                                        'printf(c);\n '
                                                                                                        '   return '
                                                                                                        'c;',
                     'path': 'C:/Users/MZS/PycharmProjects/CodeAudit/File/test.c', 'start': 3, 'end': 7}
    code = """
    int result = add(2, 3);
    return 0;
    """
    matchs = extract_function_calls(code)
    for match in matchs:
        print(match_function_calls(function_info, match))