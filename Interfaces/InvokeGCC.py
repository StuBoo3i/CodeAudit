import subprocess


def compile_code(source_file, output_file):
    """
    调用GCC编译文件
    :param source_file: 源文件
    :param output_file: 编译结果路径
    :return: 无
    """
    command = ['gcc', source_file, '-o', output_file]
    subprocess.run(command)
    return 0
