from FunctionAndVariableDetection.ExtractFunctions import process_c_files


def functionInvalidDetection(node, file_path):
    # 提取自定义函数和库函数
    custom_functions, library_functions = process_c_files(node, file_path)
    func_useless = []
    for func in custom_functions:
        if func not in library_functions:
            func_useless.append(func)
    return func_useless
