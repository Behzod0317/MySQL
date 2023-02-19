import tkinter as tk
import mysql.connector
#from .employees import *


mydb = mysql.connector.connect(
    host="127.0.0.1:3306'",
    user="root",
    password="parol178",
    database="employee_management_system"
)

# Define functions for adding, editing, and deleting employee records
def add_employee():
    name = name_entry.get()
    address = address_entry.get()
    salary = salary_entry.get()
    job_title = job_title_entry.get()
    department = department_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO employees (name, address, salary, job_title, department) VALUES (%s, %s, %s, %s, %s)"
    val = (name, address, salary, job_title, department)
    mycursor.execute(sql, val)
    mydb.commit()
    clear_entries()
    get_employees()

def edit_employee():
    selected_employee = employee_listbox.get(employee_listbox.curselection())
    if selected_employee:
        employee_id = selected_employee[0]
        name = name_entry.get()
        address = address_entry.get()
        salary = salary_entry.get()
        job_title = job_title_entry.get()
        department = department_entry.get()

        mycursor = mydb.cursor()
        sql = "UPDATE employees SET name = %s, address = %s, salary = %s, job_title = %s, department = %s WHERE id = %s"
        val = (name, address, salary, job_title, department, employee_id)
        mycursor.execute(sql, val)
        mydb.commit()
        clear_entries()
        get_employees()

def delete_employee():
    selected_employee = employee_listbox.get(employee_listbox.curselection())
    if selected_employee:
        employee_id = selected_employee[0]
        mycursor = mydb.cursor()
        sql = "DELETE FROM employees WHERE id = %s"
        val = (employee_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        clear_entries()
        get_employees()

# Define function for getting employee records
def get_employees():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM employees")
    employees = mycursor.fetchall()
    employee_listbox.delete(0, tk.END)
    for employee in employees:
        employee_listbox.insert(tk.END, employee)

# Define function for clearing entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    job_title_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title("Employee Management System")

# Create input fields
name_label = tk.Label(window, text="Name")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

address_label
