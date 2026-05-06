import pandas as pd
import numpy as np

data_names = pd.read_csv('../data/first-names.txt',header=None)
data_last = pd.read_csv('../data/last-names.txt',header=None)
data_issues = pd.read_csv('../data/list_issues.txt',header=None)
data_employees = pd.read_csv('../data/list_employees.txt',header=None)
data_passwords = pd.read_csv('../data/list_passwords.txt',header=None)

n_elements = 500

data_t = pd.DataFrame(
{
    'customername': np.random.choice(data_names[0],n_elements) + ' ' + np.random.choice(data_last[0],n_elements)
})

## email list
email_list = []
for name in data_t['customername']:
    email_list.append(name.split()[0][0] + name.split()[1] + '@gmail.com')

data_t['customeremail'] = email_list

#submit date
from random import randint
import datetime

date_list = []
startdate=datetime.date(2026,3,10)
for i in range(0,n_elements):
    date=startdate+datetime.timedelta(randint(1,20))
    date_list.append(date)
date_list = sorted(date_list)

data_t['submitteddate'] = date_list

# issues
data_t['issue'] = np.random.choice(data_issues[0],n_elements)

# employee names
employee_list = np.random.choice(data_employees[0],7)

data_t['name'] = np.random.choice(employee_list,n_elements)

# username
username_list = []
for name in data_t['name']:
    username_list.append(name.split()[0][0] + name.split()[1][:4])
    
data_t['username'] = username_list

# password
password_list = np.random.choice(data_passwords[0],7)
user_password = dict(zip(employee_list,password_list))

password_list_t = []
for name in data_t['name']:
    password_list_t.append(user_password[name])

data_t['password'] = password_list_t


# employee email
email_list = []
for name in data_t['name']:
    email_list.append(name.split()[0][0] + name.split()[1] + '@vectacorp.com')

data_t['email'] = email_list

# status
status_list = ['Open', 'In Progress', 'Closed']

data_t['status'] = np.random.choice(status_list,n_elements)

# solution

solution_list = ['vProspect','vConvert','vRetain']

data_t['solution'] = np.random.choice(solution_list,n_elements)

# roles

roles_list = ['Admin','Support','Support','Developer','Developer','Administration', 'Administration']
user_role = dict(zip(employee_list,roles_list))

roles_list_t = []
for name in data_t['name']:
    roles_list_t.append(user_role[name])

data_t['role'] = roles_list_t

data_t.to_csv('../data/VectaCorp_DF.csv', header=True)