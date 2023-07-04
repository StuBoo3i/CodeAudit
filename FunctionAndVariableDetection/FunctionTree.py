import re
from Tools.DatabaseOperation import SQL


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

    # 处理无前驱函数的情况
    for function_id in successors.keys():
        if function_id not in predecessors:
            predecessors[function_id] = []

    return predecessors


def match_function_calls(function_info, function_call):
    """
    判断函数调用是否匹配给定的函数信息
    :param function_info: 函数信息字典
    :param function_call: 函数调用信息列表，每个元素包含函数名和参数
    :return: True（匹配）或 False（不匹配）
    """
    function_name = function_info['function']
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


def func_tree_construct():
    """
    生成函数关系树
    :return: 后继函数表，以函数ID为键，前驱函数ID列表为值
    """
    mysql = SQL()
    # 后继函数表
    successors = {}
    func_infos = mysql.select_scan_function(mysql.cursor)
    for func_info in func_infos:
        matchs = extract_function_calls(func_info['function_text'])
        id = func_info['id']
        for match in matchs:
            list_sub_id = []
            for func_info_sub in func_infos:
                if match_function_calls(func_info_sub, match):
                    # print(id + ':add' + func_info_sub['id'])
                    list_sub_id.append(func_info_sub['id'])
                    break
        successors[id] = list_sub_id

    mysql.close_SQL(mysql.cursor, mysql.cnx)
    return successors


def return_preandsub():
    """
    生成前驱函数表与后驱函数表
    :return:predecessors,前驱函数表，以函数ID为键，前驱函数ID列表为值
    :return:successors,后继函数表，以函数ID为键，前驱函数ID列表为值
    """
    successors = func_tree_construct()
    predecessors = generate_predecessors(successors)

    print("后继函数表：")
    for function_id, successors_list in successors.items():
        print(f"函数名: {function_id}")
        print(f"后继函数: {successors_list}")
        print()

    print("前驱函数表：")
    for function_id, predecessors_list in predecessors.items():
        print(f"函数名: {function_id}")
        print(f"前驱函数: {predecessors_list}")
        print()
    return predecessors, successors


if __name__ == '__main__':
    return_preandsub()
