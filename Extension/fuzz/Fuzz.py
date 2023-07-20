import subprocess
import random
import re
import string


def generate_character():
    """生成包含边界值和特殊字符的自定义字符集"""
    characters = string.ascii_letters + string.digits + string.punctuation

    # 添加边界值和特殊字符
    characters += ' '  # 空格
    characters += '\n'  # 换行符
    characters += '\t'  # 制表符
    characters += '\\'  # 反斜杠

    return characters


def random_Output(length):
    """生成指定长度的随机输入"""
    character_set = generate_character()
    Output = ''.join(random.choice(character_set) for _ in range(length))
    return Output


def analyze_code(filename):
    """分析C语言代码，查找和计数不同格式的输入"""
    input_pattern = r'scanf\s*\(\s*"[^"]*"\s*(?:,\s*&?[a-zA-Z_]\w*\s*)*\);'
    expected_inputs = []

    with open(filename, 'r') as file:
        code = file.read()

    matches = re.findall(input_pattern, code)
    if matches:
        for match in matches:
            expected_inputs.append(match.strip())

    return expected_inputs


def generate_data(expected_inputs):
    """生成对应格式的随机输入"""
    input_data = ""
    for expected_input in expected_inputs:
        # 使用正则表达式匹配期望的输入格式
        matches = re.findall(r'%[dfs]', expected_input)
        if matches:
            for match in matches:
                format_type = match[1:]
                if format_type == "d":
                    random_number = random.randint(-100, 100)
                    input_data += str(random_number) + " "
                elif format_type == "f":
                    random_float = random.uniform(-100.0, 100.0)
                    input_data += str(random_float) + " "
                elif format_type == "s":
                    random_string = random_Output(random.randint(1, 100))
                    input_data += random_string + " "
            # 添加其他期望输入类型的处理逻辑

    return input_data.strip()


def is_crash(output, str):
    # 在程序异常退出时记录input_data到一个txt文件中
    if "Segmentation fault" in output:
        with open("fuzz_string.txt", "a") as file:
            file.write("Input data:" + str + "\n")
    return


def is_input_in_loop(code):
    """判断输入语句是否在循环语句的复合语句中"""
    loop_keywords = ["for", "while", "do"]
    input_functions = ["scanf"]

    for loop_keyword in loop_keywords:
        start_index = code.find(loop_keyword)
        if start_index != -1:
            code = code[start_index:]
            for input_function in input_functions:
                input_start_index = code.find(input_function)
                if input_start_index != -1:
                    code = code[input_start_index:]
                    bracket_count = 0
                    for char in code:
                        if char == '{':
                            bracket_count += 1
                        elif char == '}':
                            bracket_count -= 1
                            if bracket_count == 1:
                                return True
                    break

    return False


def run_program(input_data, file):
    """运行目标C程序并返回输出"""
    command = ['gcc', file, '-o', 'program.exe']  # 编译C程序为可执行文件
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    command = ['./program.exe']  # 运行C程序
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input_data)
    return stdout, stderr


def fuzz(filename):
    NUM_TESTS = 10
    crash_found = False

    # 检查是否在循环的复合语句中
    with open(filename, 'r') as file:
        code = file.read()
    if is_input_in_loop(code):
        print("Input statements found inside a loop.")
        return

    # 解析代码
    expected_inputs = analyze_code(filename)
    print(expected_inputs)
    i = 0
    for i in range(NUM_TESTS):
        if expected_inputs:
            i += 1
            print(i)
            input_data = generate_data(expected_inputs)
            print(input_data)
            stdout, stderr = run_program(input_data, filename)

            if is_crash(stdout, input_data) or is_crash(stderr, input_data):
                print("Crash detected!")
                crash_found = True
                break

    if crash_found:
        with open("fuzz_string.txt", "r") as file:
            content = file.read()
            if content:
                return content
    return "当前模糊测试没有发现异常字符串"


if __name__ == "__main__":
    fuzz('../../File/calculator.c')
