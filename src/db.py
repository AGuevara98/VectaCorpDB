# DATABASE LAYER

import sqlite3 as sql
from contextlib import closing
from objects import Employee, Ticket, Solution, Status, Role

# Variable global que representa el string de conexion
conn = None

# Vamos a necesitar varios métodos
# close function
# get employee function
# get employees function
# add employee function
# delete employee function

def connect():
    global conn
    if not conn: # if conn has not been set then set
        conn =sql.connect("../db/helpdesk.sqlite")
        conn.row_factory = sql.Row # returns a dict instead of a tuple
        
def close():
    if conn:
        conn.close()
    # we call from de ui moduls when the user terminate the application

### empleados
    
def make_employee(row):
    return Employee(row['employeeid'],row['name'],row['username'],
                    row['password'],row['email'],row['roleid'])

def get_employees(): # get all of the employees of the database
    query = '''SELECT * from employees'''
    with closing(conn.cursor()) as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        
    employees = []
    for row in results:
        employees.append(make_employee(row))
    return employees
    
    
def get_employee(employeeid): # get single employee of the database, needs a employee id
    query = '''SELECT * from employees WHERE employeeid=?'''
    with closing(conn.cursor()) as cursor:
        cursor.execute(query, (employeeid,))
        results = cursor.fetchone()
        
    employee = make_employee(results)
    return employee


def add_employee(employee): # needs an array that represents all of the information of the employee
    sql_query = '''INSERT OR IGNORE INTO employees (name, username, password, email, roleid)
    VALUES (?,?,?,?,?)'''
    with closing(conn.cursor()) as cursor:
        cursor.execute(sql_query, (employee.name, employee.username,
                                   employee.password, employee.email,
                                   employee.roleid)) # representa al objeto employee
        conn.commit()
    
def delete_employee(employeeid):
    sql_query = '''DELETE FROM employees WHERE employeeid=?'''
    with closing(conn.cursor()) as cursor:
        cursor.execute(sql_query, (employeeid,))
        conn.commit()

def get_employeeid_from_role(role): ### argumento role tipo string
    query = ''' SELECT roleid from roles WHERE role=?'''
    with closing(conn.cursor()) as cursor:
        cursor.execute(query, (role,))
        results = cursor.fetchone()
    return results['roleid']

## roles

def add_role(role): # needs an object that represents all of the information of the role
    sql_query = '''INSERT OR IGNORE INTO roles (role)
    VALUES (?)'''
    with closing(conn.cursor()) as cursor:
        cursor.execute(sql_query, (role.role,)) # representa al objeto employee
        conn.commit()

# solutions
def add_solution(solution): # needs an object that represents all of the information of the solutio
    sql_query = '''INSERT OR IGNORE INTO solutions (solution)
    VALUES (?)'''
    with closing(conn.cursor()) as cursor:
        cursor.execute(sql_query, (solution.solution,)) # representa al objeto employee
        conn.commit()

# status
def add_status(status): # needs an object that represents all of the information of the status
    sql_query = '''INSERT OR IGNORE INTO status (status)
    VALUES (?)'''
    with closing(conn.cursor()) as cursor:
        cursor.execute(sql_query, (status.status,)) # representa al objeto employee
        conn.commit()

# tickets
def add_tickets(ticket): # needs an object that represents all of the information of the status
    sql_query = '''INSERT OR IGNORE INTO tickets (customername,customeremail,submitteddate,issue,employeeid,statusid,solutionid)
    VALUES (?,?,?,?,?,?,?)'''
    with closing(conn.cursor()) as cursor:
        cursor.execute(sql_query, (ticket.customername, ticket.customeremail,
                                   ticket.submitteddate, ticket.issue,
                                   ticket.employeeid,ticket.statusid,ticket.solutionid)) # representa al objeto employee
        conn.commit()

def get_employeeid_from_username(username): ### argumento role tipo string
    query = ''' SELECT employeeid from employees WHERE username=?'''
    with closing(conn.cursor()) as cursor:
        cursor.execute(query, (username,))
        results = cursor.fetchone()
    return results['employeeid']

def get_statusid_from_status(status): ### argumento role tipo string
    query = ''' SELECT statusid from status WHERE status=?'''
    with closing(conn.cursor()) as cursor:
        cursor.execute(query, (status,))
        results = cursor.fetchone()
    return results['statusid']

def get_solutionid_from_solution(solution): ### argumento role tipo string
    query = ''' SELECT solutionid from solutions WHERE solution=?'''
    with closing(conn.cursor()) as cursor:
        cursor.execute(query, (solution,))
        results = cursor.fetchone()
    return results['solutionid']