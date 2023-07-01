from Interfaces.InvokeDrmemory import invoke_drmemory
from Interfaces.InvokeGCC import compile_code
from Interfaces.InvokeCppcheck import invoke_cppcheck
from Tools.RelativePath import relative_path


def Dynamic_leak_detection(source_file, output_file):
    # 调用示例
    source_file = relative_path(source_file)
    output_file = relative_path(output_file)

    # 编译C代码
    compile_code(source_file, output_file)

    # 调用示例
    output = invoke_drmemory(output_file)
    return output


def Static_leak_detection(c_code_path):
    cppcheck_output = invoke_cppcheck(relative_path(c_code_path))

    # 解析Cppcheck输出，检查是否有内存泄漏

    print(cppcheck_output)

    if "Memory leak" in cppcheck_output:
        print("Memory leaks detected.")
    else:
        print("No memory leaks detected.")
