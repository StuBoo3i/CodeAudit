import ast

string = "[['a', 'int', ['1-14', '2-9']], ['b', 'int', ['1-20', '2-13']], ['c', 'int', ['2-5', '4-12']]]"
result = ast.literal_eval(string)
print(result)

