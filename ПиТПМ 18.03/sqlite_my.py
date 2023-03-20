import sqlite3

from sqlite3 import Error
 
con = sqlite3.connect('city.db')

# Создание базы данных

# def sql_connection():
 
#     try:
 
#         con = sqlite3.connect(':memory:')
 
#         print("Connection is established: Database is created in memory")
 
#     except Error:
 
#         print(Error)
 
#     finally:
 
#         con.close()
 
# sql_connection()

# Создание таблицы "street"
 
# def sql_connection():
 
#     try:
 
#         con = sqlite3.connect('city.db')
 
#         return con
 
#     except Error:
 
#         print(Error)
 
# def sql_table(con):
 
#     cursorObj = con.cursor()
 
#     cursorObj.execute("CREATE TABLE street(id integer PRIMARY KEY, name text)")
 
#     con.commit()
 
# con = sql_connection()
# sql_table(con)

def sql_insert(con, entities):
 
    cursorObj = con.cursor()
 
    cursorObj.execute("INSERT INTO street VALUES(1, 'Pirogova')")
    cursorObj.execute("INSERT INTO street VALUES(2, 'Prokatova')")
    cursorObj.execute("INSERT INTO street VALUES(3, 'Zosimovskaya')")
    cursorObj.execute("INSERT INTO street VALUES(4, 'Leningrad')")
    cursorObj.execute("INSERT INTO street VALUES(5, 'Koneva')")
 
    con.commit()

# Закрытие соединения

con = sqlite3.connect('street.db')
 
con.close()