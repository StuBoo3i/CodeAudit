import re
from pycparser import c_parser, c_ast
from Tools.DatabaseOperation import SQL
from Tools.FormatFunctionStatements import replace_comments, function_body
from Tools.SerializationOfList import serialize, deserialize


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
        place = str(node.coord.line) + "-" + str(node.coord.column)
        usages.append((variable_name, start_line, start_col, place))
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
        if function_node.decl.type.args:
            params = function_node.decl.type.args.params
            for param in params:
                if isinstance(param, c_ast.Decl):
                    variable_name = param.name
                    variable_type = param.type.type.names[0]
                    start_line = param.coord.line
                    start_col = param.coord.column
                    place = str(param.coord.line) + "-" + str(param.coord.column)
                    declarations.append((variable_name, variable_type, start_line, start_col, place))

    # 遍历函数节点的子节点
    for child_node in function_node.body.block_items:
        # 处理变量声明
        if isinstance(child_node, c_ast.Decl) and isinstance(child_node.type, c_ast.TypeDecl):
            variable_name = child_node.name
            variable_type = child_node.type.type.names[0]
            start_line = child_node.coord.line
            start_col = child_node.coord.column
            place = str(child_node.coord.line) + "-" + str(child_node.coord.column)
            declarations.append((variable_name, variable_type, start_line, start_col, place))
        elif isinstance(child_node, c_ast.Decl) and isinstance(child_node.type, c_ast.PtrDecl):
            variable_name = child_node.name
            variable_type = child_node.type.type.type.names[0] + '*'
            start_line = child_node.coord.line
            start_col = child_node.coord.column
            place = str(child_node.coord.line) + "-" + str(child_node.coord.column)
            declarations.append((variable_name, variable_type, start_line, start_col, place))

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
    # function_name = "add"
    # function_node = None
    # for node in ast.ext:
    #     if isinstance(node, c_ast.FuncDef) and node.decl.name == function_name:
    #         function_node = node
    #         break

    # 遍历AST中的所有函数节点
    for node in ast.ext:
        if isinstance(node, c_ast.FuncDef):
            # 处理函数的AST，记录变量声明、使用和作为返回值的信息
            result = process_function_ast(node)

    # if function_node:
    #     # 处理函数的AST，记录变量声明、使用和作为返回值的信息
    #     result = process_function_ast(function_node)

    # 打印变量声明
    # print("Declarations:")
    # for declaration in result[0]:
    #     variable_name, variable_type, start_line, start_col, place = declaration
    #     print(
    #         f"Variable '{variable_name}' of type '{variable_type}' declared at line {start_line}, col {start_col}")
    #
    # # 打印变量使用
    # print("\nUsages:")
    # for usage in result[1]:
    #     variable_name, start_line, start_col, place = usage
    #     print(f"Variable '{variable_name} used at line {start_line}, col {start_col}")
    #
    # # 打印返回值
    # if result[2]:
    #     print("\nReturn Values:")
    #     for return_value in result[2]:
    #         variable_name, start_line, start_col = return_value
    #         print(
    #             f"Variable '{variable_name} returned at line {start_line}, col {start_col}")

    # else:
    #     print(f"Function '{function_name}' not found.")
    #     return None

    datas = [[list(inner_tuple) for inner_tuple in inner_list] for inner_list in result]

    return datas


def p_value_to_SQL(text):
    listss = value_scanner(text)
    lists = listss[0]
    placess = listss[1]
    datas = []

    for list in lists:
        places = [list[4]]
        for p in placess:
            if list[0] == p[0]:
                places.append(p[3])
        data = [list[0], list[1], places]
        datas.append(data)

    return datas


def scan_v_from_f():
    mysql = SQL()
    functions = mysql.select_scan_function(mysql.cursor)
    f_s = []
    for f in functions:
        v = p_value_to_SQL(replace_comments(function_body(f)))
        if len(v) > 0:
            function_v = [f['id'], v]
            f_s.append(function_v)
    print(f_s)
    for f in f_s:
        list = [f[0], str(f[1])]
        mysql.insert_value_of_function(mysql.cnx, mysql.cursor, list)

    mysql.close_SQL(mysql.cnx, mysql.cursor)
