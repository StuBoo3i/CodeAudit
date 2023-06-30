import ctypes
import gc
from Tools.RelativePath import relative_path


def leak_detection(dll_path):
    # 加载动态链接库
    lib = ctypes.CDLL(relative_path(dll_path))  # 替换为你的动态链接库文件路径

    # 定义C函数的参数类型
    lib.func1.argtypes = []
    lib.func2.argtypes = []

    # 定义C函数的返回类型
    lib.func1.restype = None
    lib.func2.restype = None

    # 设置内存分配和释放的钩子函数
    def malloc_hook(size):
        print(f"Allocated memory block of size {size} bytes")

    def free_hook(ptr):
        print(f"Freed memory block at address {ptr}")

    # 注册钩子函数
    ctypes.c_void_p.in_dll(lib, "malloc")._callbacks.append(malloc_hook)
    ctypes.c_void_p.in_dll(lib, "free")._callbacks.append(free_hook)

    # 检测内存泄漏
    def detect_memory_leak(func):
        # 清除之前的内存分配和释放钩子函数
        ctypes.c_void_p.in_dll(lib, "malloc")._callbacks = []
        ctypes.c_void_p.in_dll(lib, "free")._callbacks = []

        # 注册新的钩子函数
        ctypes.c_void_p.in_dll(lib, "malloc")._callbacks.append(malloc_hook)
        ctypes.c_void_p.in_dll(lib, "free")._callbacks.append(free_hook)

        # 调用C函数
        func()

        # 手动执行垃圾回收以确保所有的钩子函数被调用
        gc.collect()

    # 调用C函数并检测内存泄漏
    detect_memory_leak(lib.func1)
    detect_memory_leak(lib.func2)
