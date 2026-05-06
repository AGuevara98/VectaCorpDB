# OBJECT LAYER
# Queremos facilitar las cosas queremos referenciar las cosas por su nombre, username etc en lugar
# de una posicion en la tabla
# seis propiedades de este objeto que representan las variables de la base de datos

class Employee: # initial function
    def __init__(self, employeeid=0, name=None, username=None, password=None, email=None, roleid=0):
        self.employeeid = employeeid
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.roleid = roleid

class Role:
    def __init__(self, roleid=0, role=None):
        self.roleid = roleid
        self.role = role

class Solution:
    def __init__(self, solutionid=0, solution=None):
        self.solutionid = solutionid
        self.solution = solution

class Status:
    def __init__(self, statusid=0, status=None):
        self.statusid = statusid
        self.status = status

class Ticket:
    def __init__(self, ticketid=0, customername=None, customeremail=None,
                 submitteddate=None, issue=None, employeeid=0, statusid=0, solutionid=0):
        self.ticketid = ticketid
        self.customername = customername
        self.customeremail = customeremail
        self.submitteddate = submitteddate
        self.issue = issue
        self.employeeid = employeeid
        self.statusid = statusid
        self.solutionid = solutionid