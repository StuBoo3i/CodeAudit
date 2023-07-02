from FunctionAndVariableDetection.ExtractFunctions import process_c_files


def functionInvalidDetection(node, file_path):
    """
    无效函数检测
    :param node: TreeNode根节点
    :param file_path: 文件路径
    :return:无效的函数名的list
    """
    # 提取自定义函数和库函数
    custom_functions, library_functions = process_c_files(node, file_path)
    func_useless = []
    for func in custom_functions:
        if func not in library_functions:
            func_useless.append(func)
    return func_useless
