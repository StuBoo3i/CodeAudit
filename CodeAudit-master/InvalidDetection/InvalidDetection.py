from Interfaces.InvokeCppcheck import invoke_cppcheck
from Tools.RelativePath import relative_path
from Tools.FileOperation import write_to_file, print_lines


def invalid_function_detection(c_code_path):
    """
        无效函数分析
        :param c_code_path: C语言源码路径
        :return: cppcheck的分析结果
        """
    cppcheck_output = invoke_cppcheck(relative_path(c_code_path))

    # 解析Cppcheck输出，检查是否有无效函数

    return cppcheck_output


def function_position(source_file):
    """
    返回静态检测定位
    :param source_file: 检测源文件路径
    :return: 问题出现行的list
    """

    write_to_file(relative_path('File/result_i.txt'), invalid_function_detection(source_file))
    return print_lines(relative_path('File/result_i.txt'), '[InvalidDetection]')
