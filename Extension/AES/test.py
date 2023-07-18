from Tools.DatabaseOperation import SQL

mysql = SQL()
mysql.encrypt_message(mysql.cursor,mysql.cnx,"mypasswprd")