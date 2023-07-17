
from Tools.DatabaseOperation import SQL





if __name__ == "__main__":
    mysql = SQL()
    print(mysql.SQL_Login(mysql.cursor,"admin","mypasswprd"))
