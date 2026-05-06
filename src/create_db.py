import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_role(conn, project):
    """
    Create a new role into the role table
    :param conn:
    :param role:
    :return: role id
    """
    sql_query = ''' INSERT or IGNORE INTO roles (role)
             VALUES(?);'''
#    sql_query = '''INSERT INTO roles (role) VALUES(?)
#                   WHERE NOT EXISTS(SELECT * FROM roles WHERE role=Support OR role=Developer OR role=Administration OR role=Admin);'''
    cur = conn.cursor()
    cur.execute(sql_query, project)
    conn.commit()
    return cur.lastrowid

def main():
    database = "../db/helpdesk.sqlite"

    sql_create_employees_table = """ CREATE TABLE IF NOT EXISTS employees (
                                        employeeid integer PRIMARY KEY,
                                        name varchar NOT NULL,
                                        username varchar NOT NULL UNIQUE,
                                        password varchar NOT NULL,
                                        email varchar NOT NULL UNIQUE,
                                        roleid integer NOT NULL
                                    ); """

    sql_create_roles_table = """CREATE TABLE IF NOT EXISTS roles (
                                    roleid integer PRIMARY KEY,
                                    role varchar NOT NULL UNIQUE
                                );"""
    
    sql_create_tickets_table = """ CREATE TABLE IF NOT EXISTS tickets (
                                        ticketid integer PRIMARY KEY,
                                        statusid integer NOT NULL,
                                        solutionid integer NOT NULL,
                                        employeeid integer NOT NULL,
                                        issue text,
                                        customername varchar NOT NULL,
                                        customeremail varchar NOT NULL,
                                        submitteddate datetime NOT NULL
                                    ); """
    
    sql_create_solutions_table = """CREATE TABLE IF NOT EXISTS solutions (
                                    solutionid integer PRIMARY KEY,
                                    solution varchar NOT NULL UNIQUE
                                );"""
    
    sql_create_status_table = """CREATE TABLE IF NOT EXISTS status (
                                    statusid integer PRIMARY KEY,
                                    status varchar NOT NULL UNIQUE
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create employees table
        create_table(conn, sql_create_employees_table)

        # create roles table
        create_table(conn, sql_create_roles_table)
        
        # create tickets table
        create_table(conn, sql_create_tickets_table)
        
        # create solutions table
        create_table(conn, sql_create_solutions_table)
        
        # create status table
        create_table(conn, sql_create_status_table)
    else:
        print("Error! cannot create the database connection.")

    #create roles
    role_1 = ('Support',)
    role_2 = ('Developer',)
    role_3 = ('Administration',)
    role_4 = ('Admin',)
    
    create_role(conn,role_1)
    create_role(conn,role_2)
    create_role(conn,role_3)
    create_role(conn,role_4)

if __name__ == '__main__':
    main()