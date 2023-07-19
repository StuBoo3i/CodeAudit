import subprocess
import random
import string


def generate_random_input():
    """生成随机输入"""
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    return f"{num1} {num2}"


def run_target_program(input_data):
    """运行目标C程序并返回输出"""
    command = ['gcc', 'calculator.c', '-o', 'calculator.exe']  # 编译C程序为可执行文件
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    command = ['./calculator.exe']  # 运行C程序
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True)
    stdout, stderr = process.communicate(input_data)
    return stdout, stderr


def is_crash(output):
    """判断程序是否崩溃"""
    # 简单示例中不判断崩溃，留待更复杂的实现中
    return


def generate_fuzz_character_set():
    """生成fuzz字符库"""
    characters = string.digits + ' \n'
    return characters


def main():
    NUM_TESTS = 100

    for i in range(NUM_TESTS):
        print("times")
        input_data = generate_random_input()
        stdout, stderr = run_target_program(input_data)

        if is_crash(stdout) or is_crash(stderr):
            print("Crash detected!")
            print("Input data:", input_data)
            break



if __name__ == "__main__":
    main()
