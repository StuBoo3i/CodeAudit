from Interfaces.InvokeDrmemory import invoke_drmemory
from Interfaces.InvokeGCC import compile_code
from Interfaces.InvokeCppcheck import invoke_cppcheck
from Tools.FileOperation import write_to_file, print_lines
from Tools.RelativePath import relative_path


def dynamic_leak_detection(source_file, output_file):
    """
    动态内存泄漏分析
    :param source_file: 源c文件
    :param output_file: 生成的exe文件目录
    :return:Dr.memory的分析结果
    """
    # 调用示例
    source_file = relative_path(source_file)
    output_file = relative_path(output_file)

    # 编译C代码
    compile_code(source_file, output_file)

    # 调用示例
    output = invoke_drmemory(output_file)
    return output


def static_leak_detection(c_code_path):
    """
    静态内存泄漏分析
    :param c_code_path: C语言源码路径
    :return: cppcheck的分析结果
    """
    cppcheck_output = invoke_cppcheck(relative_path(c_code_path))

    # 解析Cppcheck输出，检查是否有内存泄漏

    return cppcheck_output


def static_position(source_file):
    """
    返回静态检测定位
    :param source_file: 检测源文件路径
    :return: 问题出现行的list
    """
    write_to_file(relative_path('File/result.txt'), static_leak_detection(source_file))
    return print_lines(relative_path('File/result.txt'), '[memleak]')
