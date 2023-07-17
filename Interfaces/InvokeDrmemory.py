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


if __name__ == "__main__":
    # 将Dr. Memory输出的内容作为字符串传入translate_drmemory_output函数
    drmemory_output = """
~~Dr.M~~ Dr. Memory version 2.5.19327
~~Dr.M~~ Running "E:\Data\PyCharm\CodeAudit\File/test.exe"
~~Dr.M~~ Using system call file E:\Data\Tools\DrMemory2.5\drmemory\logs\symcache\syscalls_x64.txt
~~Dr.M~~ 
~~Dr.M~~ Error #1: UNADDRESSABLE ACCESS beyond top of stack: reading 0x000000a63d5ff870-0x000000a63d5ff878 8 byte(s)
~~Dr.M~~ # 0 ___chkstk_ms                            [../../../../../src/gcc-11.2.0/libgcc/config/i386/cygwin.S:132]
~~Dr.M~~ # 1 _pei386_runtime_relocator
~~Dr.M~~ # 2 __tmainCRTStartup
~~Dr.M~~ # 3 .l_start
~~Dr.M~~ # 4 ntdll.dll!RtlUserThreadStart
~~Dr.M~~ Note: @0:00:00.088 in thread 1588
~~Dr.M~~ Note: 0x000000a63d5ff870 refers to 616 byte(s) beyond the top of the stack 0x000000a63d5ffad8
~~Dr.M~~ Note: instruction: or     $0x0000000000000000 (%rcx) -> (%rcx)
Hello, world!~~Dr.M~~ 
~~Dr.M~~ Error #2: POSSIBLE LEAK 57 direct bytes 0x000001bc808d01c0-0x000001bc808d01f9 + 0 indirect bytes
~~Dr.M~~ # 0 replace_malloc                   [D:\\a\drmemory\drmemory\common\\alloc_replace.c:2580]
~~Dr.M~~ # 1 msvcrt.dll!malloc_crt
~~Dr.M~~ # 2 msvcrt.dll!_setargv  
~~Dr.M~~ # 3 msvcrt.dll!_getmainargs
~~Dr.M~~ # 4 pre_cpp_init
~~Dr.M~~ # 5 msvcrt.dll!initterm  
~~Dr.M~~ # 6 __tmainCRTStartup
~~Dr.M~~ # 7 .l_start
~~Dr.M~~ # 8 ntdll.dll!RtlUserThreadStart
~~Dr.M~~ 
~~Dr.M~~ Error #3: REACHABLE LEAK 16 direct bytes 0x000001bc808d0250-0x000001bc808d0260 + 0 indirect bytes
~~Dr.M~~ <memory was allocated before tool took control>
~~Dr.M~~ 
~~Dr.M~~ Error #4: REACHABLE LEAK 16 direct bytes 0x000001bc808d0280-0x000001bc808d0290 + 0 indirect bytes
~~Dr.M~~ <memory was allocated before tool took control>
~~Dr.M~~ 
~~Dr.M~~ Error #5: REACHABLE LEAK 40 direct bytes 0x000001bc808d02b0-0x000001bc808d02d8 + 0 indirect bytes
~~Dr.M~~ <memory was allocated before tool took control>
~~Dr.M~~ 
~~Dr.M~~ Error #6: REACHABLE LEAK 4096 direct bytes 0x000001bc808d0300-0x000001bc808d1300 + 0 indirect bytes
~~Dr.M~~ <memory was allocated before tool took control>
~~Dr.M~~ 
~~Dr.M~~ Error #7: LEAK 10 direct bytes 0x000001bc808d1320-0x000001bc808d132a + 0 indirect bytes
~~Dr.M~~ # 0 replace_malloc               [D:\\a\drmemory\drmemory\common\\alloc_replace.c:2580]
~~Dr.M~~ # 1 func2   
~~Dr.M~~ # 2 main    
~~Dr.M~~ 
~~Dr.M~~ ERRORS FOUND:
~~Dr.M~~       1 unique,     2 total unaddressable access(es)
~~Dr.M~~       0 unique,     0 total uninitialized access(es)
~~Dr.M~~       0 unique,     0 total invalid heap argument(s)
~~Dr.M~~       0 unique,     0 total GDI usage error(s)
~~Dr.M~~       0 unique,     0 total handle leak(s)
~~Dr.M~~       0 unique,     0 total warning(s)
~~Dr.M~~       1 unique,     1 total,     10 byte(s) of leak(s)
~~Dr.M~~       1 unique,     1 total,     57 byte(s) of possible leak(s)
~~Dr.M~~       4 unique,     4 total,   4168 byte(s) of still-reachable allocation(s)
~~Dr.M~~ NO ERRORS IGNORED
~~Dr.M~~ Details: E:\Data\Tools\DrMemory2.5\drmemory\logs\DrMemory-test.exe.6328.000\\results.txt
    """

    translated_output = translate(drmemory_output)
    print(translated_output)
