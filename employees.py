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

c.execute("""CREATE TABLE employees (
    
    name VARCHAR(50) NOT NULL,
    address VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    job_title VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL
)""")
