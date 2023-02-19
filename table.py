
# from .sql import extract_table_columns

# CREATE TABLE my_table (
#   id INTEGER PRIMARY KEY,
#   name TEXT,
#   age INTEGER
# );
# table_name, columns = extract_table_columns("CREATE TABLE my_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);")
# print(table_name)  # prints "my_table"
# print(columns)  # prints ["id", "name", "age"]

import sqlite3
from sql import *
import pandas as pd

conn = sqlite3.connect('Employee.db')

c=conn.cursor()
# c.execute(""" CREATE TABLE employees(
#       first text,
#       last text,

#       pay integer
#   )""")

# c.execute("""CREATE TABLE employees (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(50) NOT NULL,
#     address VARCHAR(100) NOT NULL,
#     salary DECIMAL(10,2) NOT NULL,
#     job_title VARCHAR(50) NOT NULL,
#     department VARCHAR(50) NOT NULL
# )""")
emp_1 = extract_table_columns('Shavkat')
emp_2 = Employee('Risqinboy','Tojiboyev',1200000)
emp_3 = Employee('Behruz','Nabijonov',12000000)
emp_4 = Employee('Azizxon','Tojixonov',12300000)
emp_5 = Employee('Oybek','Valiyev',12300000)

c.execute("INSERT INTO employees VALUES('Behzod','Hoshimov',13500000)")
c.execute("INSERT INTO employees VALUES('{}','{}',{})".format(emp_1.first,emp_1.last,emp_1.pay))

conn.commit()

c.execute("INSERT INTO employees VALUES(:first, :last, :pay)",(emp_5.first,emp_5.last,emp_5.pay))
#c.execute("INSERT INTO employees VALUES(:first, :last, :pay)",(emp_5.first,emp_2.last,emp_2.pay))
conn.commit()
c.execute("SELECT rowid,* FROM employees")
item = c.fetchall()

for el in item:
    print(el)

conn.commit()
conn.close()

columns = ["Id","Name","Lastname","Salary $"]
df = pd.DataFrame(data= item, columns=columns)
df.to_csv("Employees.csv", index = False)