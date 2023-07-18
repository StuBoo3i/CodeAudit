import subprocess


def invoke_drmemory(program_path):
    """
    调用dr.memory进行动态内存泄漏分析
    :param program_path: 可执行程序的路径
    :return: 分析结果
    """
    command = ['drmemory', '-batch', '-show_reachable', '--', program_path]
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    return translate(output.decode('utf-8'))


def translate(output):
    translations = {
        "~~Dr.M~~": "",
        "Running": "运行中",
        "Using system call file": "使用系统调用文件",
        "Error #": "错误 #",
        "UNADDRESSABLE ACCESS": "非法内存访问",
        "POSSIBLE LEAK": "可能的内存泄漏",
        "REACHABLE LEAK": "可达的内存泄漏",
        "LEAK": "内存泄漏",
        "ERRORS FOUND": "检测到的问题",
        "total unaddressable access(es)": "个非法内存访问",
        "total uninitialized access(es)": "个未初始化内存访问",
        "total invalid heap argument(s)": "个无效的堆参数",
        "total GDI usage error(s)": "个GDI使用错误",
        "total handle leak(s)": "个句柄泄漏",
        "total warning(s)": "个警告",
        "byte(s) of leak(s)": "个字节的内存泄漏",
        "byte(s) of possible leak(s)": "个字节的可能内存泄漏",
        "byte(s) of still-reachable allocation(s)": "个字节的可达内存分配",
        "NO ERRORS IGNORED": "没有忽略的错误",
        "\\": "\\\\",
    }

    for key, value in translations.items():
        output = output.replace(key, value)

    return output
