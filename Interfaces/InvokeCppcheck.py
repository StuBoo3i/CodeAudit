import subprocess


def invoke_cppcheck(c_code_path):
    """
    调用cppcheck进行静态内存泄漏分析
    :param c_code_path: 源文件路径
    :return: 分析结果
    """
    cppcheck_command = [r"E:\Data\Tools\Cppcheck\cppcheck.exe", "--platform=win64", "--enable=all",
                        "--inconclusive", c_code_path]
    result = subprocess.getoutput(cppcheck_command)
    return result
