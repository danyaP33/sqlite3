import sqlite3
 
from sqlite3 import Error

con = sqlite3.connect('mydatabase.db')

# Написанный ниже код выполнен, но я решил оставить его здесь закомментированным.

# #Создание соединения
 
# def sql_connection():
 
#     try:
 
#         con = sqlite3.connect('mydatabase.db')
 
#         return con
 
#     except Error:
 
#         print(Error)
 
#  #Создание таблицы

# def sql_table(con):
 
#     cursorObj = con.cursor()
 
#     cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
 
#     con.commit()
 
# con = sql_connection()
# sql_table(con)

#Добавление данных в таблицу

def sql_insert(con, entities):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
 
    con.commit()
 
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
 
sql_insert(con, entities)

#Обновление таблицы

def sql_update(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
 
    con.commit()
 
sql_update(con)

#Выбор всех данных в таблице

def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT * FROM employees')
 
    rows = cursorObj.fetchall()
 
    for row in rows:
 
        print(row)
 
sql_fetch(con)

#Вывод списка таблиц 

def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
 
    print(cursorObj.fetchall())
 
sql_fetch(con)

#Удаление таблицы

def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('DROP table if exists employees')
 
    con.commit()
 
sql_fetch(con)

#Закрытие соединения

con = sqlite3.connect('mydatabase.db')
 
con.close()