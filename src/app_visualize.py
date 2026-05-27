import streamlit as st
import pandas as pd
import db
from objects import Employee

# Initialize session state for multi-step flows
if 'delete_employee' not in st.session_state:
    st.session_state.delete_employee = None
if 'update_employee' not in st.session_state:
    st.session_state.update_employee = None

def add_employee(name, email, role, username, password):
    employee = Employee(name=name,
                        email=email,
                        roleid=db.get_roleid_from_role(str(role)),
                        username=username,
                        password=password)
    db.add_employee(employee)

def update_employee_db(employeeid, name, email, role, username, password):
    employee = Employee(employeeid=employeeid,
                        name=name,
                        email=email,
                        roleid=db.get_roleid_from_role(str(role)),
                        username=username,
                        password=password)
    db.update_employee(employee)


st.title("Employee Vecta Corp Menu")

db.connect()

opciones = ["View", "Add", "Delete", "Update"]
selection = st.selectbox("Selecciona una opción:", opciones)

if selection == "View":
    st.write("VECTA CORP HELP DESK EMPLOYEES")
    employees = db.get_employees()

    columns = ["employeeid", "name", "username", "password", "email", "role"]
    df = pd.DataFrame(columns=columns)

    for employee in employees:
        new_data = {
            'employeeid': [employee.employeeid],
            'name': [employee.name],
            'username': [employee.username],
            'password': [employee.password],
            'email': [employee.email],
            'role': [db.get_role_from_roleid(employee.roleid)]
        }
        new_df = pd.DataFrame(new_data)
        df = pd.concat([df, new_df])

    st.table(df)

if selection == "Add":
    with st.form(key='Add new employee'):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input(label="Name")
            email = st.text_input(label="Email")
            role = st.text_input(label="Role")

        with col2:
            username = st.text_input(label="UserName")
            password = st.text_input(label="Password")

        submitted = st.form_submit_button(label="Submit", type='primary')

        if submitted:
            add_employee(name, email, role, username, password)
            st.success(f"Employee '{name}' added successfully!")

if selection == "Delete":
    employeeid_input = st.text_input(label="Employee ID:", key="delete_id_input")

    if st.button("Show Employee", key="delete_show_btn"):
        if employeeid_input:
            employee = db.get_employee(int(employeeid_input))
            st.session_state.delete_employee = employee

    if st.session_state.delete_employee is not None:
        emp = st.session_state.delete_employee
        st.write(f"**Name:** {emp.name}")
        st.write(f"**Username:** {emp.username}")
        st.write(f"**Email:** {emp.email}")
        st.write(f"**Role:** {db.get_role_from_roleid(emp.roleid)}")

        st.subheader("Are you sure you want to delete this employee?")

        if st.button("Delete", type="primary", key="delete_confirm_btn"):
            db.delete_employee(emp.employeeid)
            st.success(f"Employee '{emp.name}' has been removed.")
            st.session_state.delete_employee = None

if selection == "Update":
    employeeid_input = st.text_input(label="Employee ID:", key="update_id_input")

    if st.button("Show Employee", key="update_show_btn"):
        if employeeid_input:
            employee = db.get_employee(int(employeeid_input))
            st.session_state.update_employee = employee

    if st.session_state.update_employee is not None:
        emp = st.session_state.update_employee

        with st.form("Update Employee Form"):
            col1, col2 = st.columns(2)

            with col1:
                name = st.text_input(label="Name", value=emp.name)
                email = st.text_input(label="Email", value=emp.email)
                role = st.text_input(label="Role", value=db.get_role_from_roleid(emp.roleid))

            with col2:
                username = st.text_input(label="UserName", value=emp.username)
                password = st.text_input(label="Password", value=emp.password)

            update_button = st.form_submit_button(label="Update", type="primary")

            if update_button:
                update_employee_db(emp.employeeid, name, email, role, username, password)
                st.success(f"Employee '{name}' updated successfully!")
                st.session_state.update_employee = None
