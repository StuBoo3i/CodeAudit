import subprocess


def invoke_drmemory(program_path):
    """
    调用dr.memory进行动态内存泄漏分析
    :param program_path: 可执行程序的路径
    :return: 分析结果
    """
    command = ['drmemory', '-batch', '-show_reachable', '--', program_path]
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    return output.decode('utf-8')


