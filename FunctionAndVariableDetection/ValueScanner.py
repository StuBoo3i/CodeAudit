import re
from pycparser import c_parser, c_ast


def process_node(node, usages):
    """
    迭代函数
    :param node: 节点
    :param usages: 容器
    :return: 无
    """
    if isinstance(node, c_ast.Assignment) and isinstance(node, c_ast.BinaryOp):
        process_node(node.lvalue, usages)
        process_node(node.rvalue, usages)
    elif isinstance(node, c_ast.ID):
        variable_name = node.name
        start_line = node.coord.line
        start_col = node.coord.column
        usages.append((variable_name, start_line, start_col))
    elif isinstance(node, c_ast.FuncCall):
        # 跳过函数调用节点
        pass
    elif hasattr(node, "children"):
        # 遍历节点的子节点
        for child_name, child in node.children():
            # 跳过父节点中的 "lvalue" 和 "rvalue" 属性
            if child_name not in ['lvalue', 'rvalue']:
                process_node(child, usages)
            else:
                process_node(child, usages)


def process_function_ast(function_node):
    """
    处理函数的AST，记录变量声明、使用和作为返回值的信息
    :param function_node: 函数节点
    :return: 包含变量声明、使用和作为返回值的信息的列表
    """
    result = []
    declarations = []
    usages = []
    return_values = []
    # 处理函数参数
    if isinstance(function_node, c_ast.FuncDef):
        params = function_node.decl.type.args.params
        for param in params:
            if isinstance(param, c_ast.Decl):
                variable_name = param.name
                start_line = param.coord.line
                start_col = param.coord.column
                declarations.append((variable_name, start_line, start_col))

    # 遍历函数节点的子节点
    for child_node in function_node.body.block_items:
        # 处理变量声明
        if isinstance(child_node, c_ast.Decl) and isinstance(child_node.type, c_ast.TypeDecl):
            variable_name = child_node.name
            start_line = child_node.coord.line
            start_col = child_node.coord.column
            declarations.append((variable_name, start_line, start_col))

        # 处理变量使用
        process_node(child_node, usages)

        # 处理函数返回值
        if isinstance(child_node, c_ast.Return):
            if isinstance(child_node.expr, c_ast.ID):
                variable_name = child_node.expr.name
                start_line = child_node.expr.coord.line
                start_col = child_node.expr.coord.column
                return_values.append((variable_name, start_line, start_col))

    result.append(declarations)
    result.append(usages)
    result.append(return_values)
    return result


def value_scanner(text):
    """
    传入代扫描函数文本扫描其中的变量
    :param text: 代扫描函数文本
    :return: 包含变量声明、使用和作为返回值的信息的列表
    """

    # 创建C语言解析器
    parser = c_parser.CParser()

    # 解析源代码为AST
    ast = parser.parse(text)

    # 获取函数"add"的AST
    function_name = "add"
    function_node = None
    for node in ast.ext:
        if isinstance(node, c_ast.FuncDef) and node.decl.name == function_name:
            function_node = node
            break

    if function_node:
        # 处理函数的AST，记录变量声明、使用和作为返回值的信息
        result = process_function_ast(function_node)

        # 打印变量声明
        print("Declarations:")
        for declaration in result[0]:
            print(f"Variable '{declaration[0]}' declared at line {declaration[1]}, col {declaration[2]}")

        # 打印变量使用
        print("\nUsages:")
        for usage in result[1]:
            print(f"Variable '{usage[0]}' used at line {usage[1]}, col {usage[2]}")

        # 打印返回值
        if result[2]:
            print("\nReturn Values:")
            for return_value in result[2]:
                print(f"Variable '{return_value[0]}' returned at line {return_value[1]}, col {return_value[2]}")

    else:
        print(f"Function '{function_name}' not found.")

    return result

def analyze_type(text):
    functions = re.findall(r'\b\w+\s+\w+\([^)]*\)\s*{[^}]*}', text)  # 正则表达式匹配函数定义
    variables = {}

    for function in functions:
        name = re.search(r'\b\w+\s+\w+', function).group()  # 获取函数名称
        variables[name] = {}

        # 提取函数参数
        parameters = re.findall(r'\b\w+\s+\w+', function[:function.index('{')])
        for param in parameters:
            param_type, param_name = param.split()
            variables[name][param_name] = param_type

        # 提取局部变量
        local_vars = re.findall(r'\b\w+\s+\w+;', function)
        for var in local_vars:
            var_type, var_name = var[:-1].split()
            variables[name][var_name] = var_type

    return variables


