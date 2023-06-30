import mysql.connector
from RelativePath import relative_path
# 连接到数据库
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="100221",
    database="code_audit"
)
cursor = conn.cursor()


# 从文件中读取数据
file_path = relative_path('Tools/CLanguageFunction.txt')
with open(file_path, 'r', encoding='UTF-8') as file:
    for line_number, line in enumerate(file, start=1):
        if line_number < 3:
            continue

        try:
            function, severity, solution = line.strip().split('\t')
        except ValueError:
            print(f"Skipping line {line_number} due to incorrect format: {line}")
            continue

        # 插入数据
        insert_query = "INSERT INTO c_function (`function`, severity, solution) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (function, severity, solution))

# 提交更改并关闭连接
conn.commit()
conn.close()
