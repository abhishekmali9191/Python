import pandas as pd
from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

#setup sqlalchemy
engine = create_engine('sqlite:///employee4.db',echo=True)
Base = declarative_base()

#define the employee model
class Employee(Base):
    __tablename__ = 'employees'
    #define columns
    employee_id = Column(Integer, primary_key=True, autoincrement=True) #Ensure primary key by 1
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
#create the table
def create_table():
    Base.metadata.create_all(engine)
    print("Table created successfully")
#insert sample data
def insert_sample_data():
    Session = sessionmaker(bind=engine)
    session = Session()
    #sample data
    employees = [
        Employee(name='John Doe', position='Manager', salary=50000),
        Employee(name='Jane Smith', position='Developer', salary=60000),
        Employee(name='Alice Johnson', position='Designer', salary=55000),
        Employee(name='Bob Brown', position='Developer', salary=62000)
    ]

    #Add and commit data
    session.add_all(employees)
    session.commit()
    print("Sample data inserted successfully")
    session.close()
#read data into a pandas dataframe
def read_data():
    #load data into DataFrame
    df = pd.read_sql_table('employees',engine)
    return df
#update data in the dataframe
def update_salary(df, employee_id, new_salary):
    df.loc[df['employee_id'] == employee_id, 'salary'] = new_salary
    return df
#delete data from the dataframe
def delete_employee(df, employee_id):
    df = df[df['employee_id'] != employee_id]
    return df
#Write updated data back to the database
def write_to_database(df):
    df.to_sql('employees', engine, if_exists='replace', index=False)
    print("Updated data written to database successfully")
#main function to perform the assignment task
def main():
    #create table and insert data(run only once)
    create_table()
    insert_sample_data()
    #read data
    df = read_data()
    print("Original data:")
    print(df)

    #update salary for employee with ID 2
    df = update_salary(df, employee_id=2,new_salary=65000)
    print("\nUpdated data:")
    print(df)

    #write updated data back in df
    write_to_database(df)
    print("\nUpdated data written to database:")

    #Read data
    df = read_data()
    print("Updated data frame ")
    print(df)

if __name__ == '__main__':
    main()
    
    
# #########################################################################
# OUTPUT
# 2024-09-14 10:29:26,982 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# INFO:sqlalchemy.engine.Engine:BEGIN (implicit)
# 2024-09-14 10:29:26,986 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_info("employees")
# 2024-09-14 10:29:26,990 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:26,994 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA temp.table_info("employees")
# 2024-09-14 10:29:26,996 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:26,999 INFO sqlalchemy.engine.Engine 
# CREATE TABLE employees (
# 	employee_id INTEGER NOT NULL, 
# 	name VARCHAR NOT NULL, 
# 	position VARCHAR NOT NULL, 
# 	salary FLOAT NOT NULL, 
# 	PRIMARY KEY (employee_id)
# )


# INFO:sqlalchemy.engine.Engine:
# CREATE TABLE employees (
# 	employee_id INTEGER NOT NULL, 
# 	name VARCHAR NOT NULL, 
# 	position VARCHAR NOT NULL, 
# 	salary FLOAT NOT NULL, 
# 	PRIMARY KEY (employee_id)
# )


# 2024-09-14 10:29:27,002 INFO sqlalchemy.engine.Engine [no key 0.00215s] ()
# INFO:sqlalchemy.engine.Engine:[no key 0.00215s] ()
# 2024-09-14 10:29:27,017 INFO sqlalchemy.engine.Engine COMMIT
# INFO:sqlalchemy.engine.Engine:COMMIT
# Table created successfully
# 2024-09-14 10:29:27,021 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# INFO:sqlalchemy.engine.Engine:BEGIN (implicit)
# 2024-09-14 10:29:27,026 INFO sqlalchemy.engine.Engine INSERT INTO employees (name, position, salary) VALUES (?, ?, ?) RETURNING employee_id
# INFO:sqlalchemy.engine.Engine:INSERT INTO employees (name, position, salary) VALUES (?, ?, ?) RETURNING employee_id
# 2024-09-14 10:29:27,029 INFO sqlalchemy.engine.Engine [generated in 0.00026s (insertmanyvalues) 1/4 (ordered; batch not supported)] ('John Doe', 'Manager', 50000.0)
# INFO:sqlalchemy.engine.Engine:[generated in 0.00026s (insertmanyvalues) 1/4 (ordered; batch not supported)] ('John Doe', 'Manager', 50000.0)
# 2024-09-14 10:29:27,031 INFO sqlalchemy.engine.Engine INSERT INTO employees (name, position, salary) VALUES (?, ?, ?) RETURNING employee_id
# INFO:sqlalchemy.engine.Engine:INSERT INTO employees (name, position, salary) VALUES (?, ?, ?) RETURNING employee_id
# 2024-09-14 10:29:27,033 INFO sqlalchemy.engine.Engine [insertmanyvalues 2/4 (ordered; batch not supported)] ('Jane Smith', 'Developer', 60000.0)
# INFO:sqlalchemy.engine.Engine:[insertmanyvalues 2/4 (ordered; batch not supported)] ('Jane Smith', 'Developer', 60000.0)
# 2024-09-14 10:29:27,036 INFO sqlalchemy.engine.Engine INSERT INTO employees (name, position, salary) VALUES (?, ?, ?) RETURNING employee_id
# INFO:sqlalchemy.engine.Engine:INSERT INTO employees (name, position, salary) VALUES (?, ?, ?) RETURNING employee_id
# 2024-09-14 10:29:27,038 INFO sqlalchemy.engine.Engine [insertmanyvalues 3/4 (ordered; batch not supported)] ('Alice Johnson', 'Designer', 55000.0)
# INFO:sqlalchemy.engine.Engine:[insertmanyvalues 3/4 (ordered; batch not supported)] ('Alice Johnson', 'Designer', 55000.0)
# 2024-09-14 10:29:27,040 INFO sqlalchemy.engine.Engine INSERT INTO employees (name, position, salary) VALUES (?, ?, ?) RETURNING employee_id
# INFO:sqlalchemy.engine.Engine:INSERT INTO employees (name, position, salary) VALUES (?, ?, ?) RETURNING employee_id
# 2024-09-14 10:29:27,042 INFO sqlalchemy.engine.Engine [insertmanyvalues 4/4 (ordered; batch not supported)] ('Bob Brown', 'Developer', 62000.0)
# INFO:sqlalchemy.engine.Engine:[insertmanyvalues 4/4 (ordered; batch not supported)] ('Bob Brown', 'Developer', 62000.0)
# 2024-09-14 10:29:27,045 INFO sqlalchemy.engine.Engine COMMIT
# INFO:sqlalchemy.engine.Engine:COMMIT
# Sample data inserted successfully
# 2024-09-14 10:29:27,058 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# INFO:sqlalchemy.engine.Engine:BEGIN (implicit)
# 2024-09-14 10:29:27,060 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_info("employees")
# 2024-09-14 10:29:27,062 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,065 INFO sqlalchemy.engine.Engine SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite~_%' ESCAPE '~' ORDER BY name
# INFO:sqlalchemy.engine.Engine:SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite~_%' ESCAPE '~' ORDER BY name
# 2024-09-14 10:29:27,067 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,069 INFO sqlalchemy.engine.Engine SELECT name FROM sqlite_master WHERE type='view' AND name NOT LIKE 'sqlite~_%' ESCAPE '~' ORDER BY name
# INFO:sqlalchemy.engine.Engine:SELECT name FROM sqlite_master WHERE type='view' AND name NOT LIKE 'sqlite~_%' ESCAPE '~' ORDER BY name
# 2024-09-14 10:29:27,071 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,074 INFO sqlalchemy.engine.Engine PRAGMA main.table_xinfo("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_xinfo("employees")
# 2024-09-14 10:29:27,076 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,079 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# INFO:sqlalchemy.engine.Engine:SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# 2024-09-14 10:29:27,081 INFO sqlalchemy.engine.Engine [raw sql] ('employees',)
# INFO:sqlalchemy.engine.Engine:[raw sql] ('employees',)
# 2024-09-14 10:29:27,084 INFO sqlalchemy.engine.Engine PRAGMA main.foreign_key_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.foreign_key_list("employees")
# 2024-09-14 10:29:27,086 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,088 INFO sqlalchemy.engine.Engine PRAGMA temp.foreign_key_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA temp.foreign_key_list("employees")
# 2024-09-14 10:29:27,090 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,093 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# INFO:sqlalchemy.engine.Engine:SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# 2024-09-14 10:29:27,095 INFO sqlalchemy.engine.Engine [raw sql] ('employees',)
# INFO:sqlalchemy.engine.Engine:[raw sql] ('employees',)
# 2024-09-14 10:29:27,097 INFO sqlalchemy.engine.Engine PRAGMA main.index_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.index_list("employees")
# 2024-09-14 10:29:27,099 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,102 INFO sqlalchemy.engine.Engine PRAGMA temp.index_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA temp.index_list("employees")
# 2024-09-14 10:29:27,104 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,106 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_info("employees")
# 2024-09-14 10:29:27,108 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,111 INFO sqlalchemy.engine.Engine PRAGMA main.index_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.index_list("employees")
# 2024-09-14 10:29:27,113 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,115 INFO sqlalchemy.engine.Engine PRAGMA temp.index_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA temp.index_list("employees")
# 2024-09-14 10:29:27,117 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,119 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_info("employees")
# 2024-09-14 10:29:27,121 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,127 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# INFO:sqlalchemy.engine.Engine:SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# 2024-09-14 10:29:27,129 INFO sqlalchemy.engine.Engine [raw sql] ('employees',)
# INFO:sqlalchemy.engine.Engine:[raw sql] ('employees',)
# 2024-09-14 10:29:27,134 INFO sqlalchemy.engine.Engine SELECT employees.employee_id, employees.name, employees.position, employees.salary 
# FROM employees
# INFO:sqlalchemy.engine.Engine:SELECT employees.employee_id, employees.name, employees.position, employees.salary 
# FROM employees
# 2024-09-14 10:29:27,136 INFO sqlalchemy.engine.Engine [generated in 0.00228s] ()
# INFO:sqlalchemy.engine.Engine:[generated in 0.00228s] ()
# 2024-09-14 10:29:27,173 INFO sqlalchemy.engine.Engine COMMIT
# INFO:sqlalchemy.engine.Engine:COMMIT
# Original data:
#    employee_id           name   position   salary
# 0            1       John Doe    Manager  50000.0
# 1            2     Jane Smith  Developer  60000.0
# 2            3  Alice Johnson   Designer  55000.0
# 3            4      Bob Brown  Developer  62000.0

# Updated data:
#    employee_id           name   position   salary
# 0            1       John Doe    Manager  50000.0
# 1            2     Jane Smith  Developer  65000.0
# 2            3  Alice Johnson   Designer  55000.0
# 3            4      Bob Brown  Developer  62000.0
# 2024-09-14 10:29:27,211 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# INFO:sqlalchemy.engine.Engine:BEGIN (implicit)
# 2024-09-14 10:29:27,223 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_info("employees")
# 2024-09-14 10:29:27,227 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,230 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_info("employees")
# 2024-09-14 10:29:27,232 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,235 INFO sqlalchemy.engine.Engine SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite~_%' ESCAPE '~' ORDER BY name
# INFO:sqlalchemy.engine.Engine:SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite~_%' ESCAPE '~' ORDER BY name
# 2024-09-14 10:29:27,237 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,240 INFO sqlalchemy.engine.Engine SELECT name FROM sqlite_master WHERE type='view' AND name NOT LIKE 'sqlite~_%' ESCAPE '~' ORDER BY name
# INFO:sqlalchemy.engine.Engine:SELECT name FROM sqlite_master WHERE type='view' AND name NOT LIKE 'sqlite~_%' ESCAPE '~' ORDER BY name
# 2024-09-14 10:29:27,242 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,244 INFO sqlalchemy.engine.Engine PRAGMA main.table_xinfo("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_xinfo("employees")
# 2024-09-14 10:29:27,246 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,249 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# INFO:sqlalchemy.engine.Engine:SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# 2024-09-14 10:29:27,251 INFO sqlalchemy.engine.Engine [raw sql] ('employees',)
# INFO:sqlalchemy.engine.Engine:[raw sql] ('employees',)
# 2024-09-14 10:29:27,253 INFO sqlalchemy.engine.Engine PRAGMA main.foreign_key_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.foreign_key_list("employees")
# 2024-09-14 10:29:27,255 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,257 INFO sqlalchemy.engine.Engine PRAGMA temp.foreign_key_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA temp.foreign_key_list("employees")
# 2024-09-14 10:29:27,259 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,262 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# INFO:sqlalchemy.engine.Engine:SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# 2024-09-14 10:29:27,264 INFO sqlalchemy.engine.Engine [raw sql] ('employees',)
# INFO:sqlalchemy.engine.Engine:[raw sql] ('employees',)
# 2024-09-14 10:29:27,266 INFO sqlalchemy.engine.Engine PRAGMA main.index_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.index_list("employees")
# 2024-09-14 10:29:27,269 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,271 INFO sqlalchemy.engine.Engine PRAGMA temp.index_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA temp.index_list("employees")
# 2024-09-14 10:29:27,273 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,275 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_info("employees")
# 2024-09-14 10:29:27,277 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,280 INFO sqlalchemy.engine.Engine PRAGMA main.index_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.index_list("employees")
# 2024-09-14 10:29:27,282 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,284 INFO sqlalchemy.engine.Engine PRAGMA temp.index_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA temp.index_list("employees")
# 2024-09-14 10:29:27,286 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,289 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_info("employees")
# 2024-09-14 10:29:27,291 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,293 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# INFO:sqlalchemy.engine.Engine:SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# 2024-09-14 10:29:27,296 INFO sqlalchemy.engine.Engine [raw sql] ('employees',)
# INFO:sqlalchemy.engine.Engine:[raw sql] ('employees',)
# 2024-09-14 10:29:27,299 INFO sqlalchemy.engine.Engine 
# DROP TABLE employees
# INFO:sqlalchemy.engine.Engine:
# DROP TABLE employees
# 2024-09-14 10:29:27,302 INFO sqlalchemy.engine.Engine [no key 0.00221s] ()
# INFO:sqlalchemy.engine.Engine:[no key 0.00221s] ()
# 2024-09-14 10:29:27,320 INFO sqlalchemy.engine.Engine 
# CREATE TABLE employees (
# 	employee_id BIGINT, 
# 	name TEXT, 
# 	position TEXT, 
# 	salary FLOAT
# )


# INFO:sqlalchemy.engine.Engine:
# CREATE TABLE employees (
# 	employee_id BIGINT, 
# 	name TEXT, 
# 	position TEXT, 
# 	salary FLOAT
# )


# 2024-09-14 10:29:27,323 INFO sqlalchemy.engine.Engine [no key 0.00227s] ()
# INFO:sqlalchemy.engine.Engine:[no key 0.00227s] ()
# 2024-09-14 10:29:27,370 INFO sqlalchemy.engine.Engine INSERT INTO employees (employee_id, name, position, salary) VALUES (?, ?, ?, ?)
# INFO:sqlalchemy.engine.Engine:INSERT INTO employees (employee_id, name, position, salary) VALUES (?, ?, ?, ?)
# 2024-09-14 10:29:27,383 INFO sqlalchemy.engine.Engine [generated in 0.01325s] [(1, 'John Doe', 'Manager', 50000.0), (2, 'Jane Smith', 'Developer', 65000.0), (3, 'Alice Johnson', 'Designer', 55000.0), (4, 'Bob Brown', 'Developer', 62000.0)]
# INFO:sqlalchemy.engine.Engine:[generated in 0.01325s] [(1, 'John Doe', 'Manager', 50000.0), (2, 'Jane Smith', 'Developer', 65000.0), (3, 'Alice Johnson', 'Designer', 55000.0), (4, 'Bob Brown', 'Developer', 62000.0)]
# 2024-09-14 10:29:27,388 INFO sqlalchemy.engine.Engine COMMIT
# INFO:sqlalchemy.engine.Engine:COMMIT
# Updated data written to database successfully

# Updated data written to database:
# 2024-09-14 10:29:27,446 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# INFO:sqlalchemy.engine.Engine:BEGIN (implicit)
# 2024-09-14 10:29:27,454 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_info("employees")
# 2024-09-14 10:29:27,458 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,464 INFO sqlalchemy.engine.Engine SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite~_%' ESCAPE '~' ORDER BY name
# INFO:sqlalchemy.engine.Engine:SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite~_%' ESCAPE '~' ORDER BY name
# 2024-09-14 10:29:27,467 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,472 INFO sqlalchemy.engine.Engine SELECT name FROM sqlite_master WHERE type='view' AND name NOT LIKE 'sqlite~_%' ESCAPE '~' ORDER BY name
# INFO:sqlalchemy.engine.Engine:SELECT name FROM sqlite_master WHERE type='view' AND name NOT LIKE 'sqlite~_%' ESCAPE '~' ORDER BY name
# 2024-09-14 10:29:27,478 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,483 INFO sqlalchemy.engine.Engine PRAGMA main.table_xinfo("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_xinfo("employees")
# 2024-09-14 10:29:27,487 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,491 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# INFO:sqlalchemy.engine.Engine:SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# 2024-09-14 10:29:27,494 INFO sqlalchemy.engine.Engine [raw sql] ('employees',)
# INFO:sqlalchemy.engine.Engine:[raw sql] ('employees',)
# 2024-09-14 10:29:27,551 INFO sqlalchemy.engine.Engine PRAGMA main.foreign_key_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.foreign_key_list("employees")
# 2024-09-14 10:29:27,558 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,562 INFO sqlalchemy.engine.Engine PRAGMA temp.foreign_key_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA temp.foreign_key_list("employees")
# 2024-09-14 10:29:27,567 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,570 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# INFO:sqlalchemy.engine.Engine:SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# 2024-09-14 10:29:27,580 INFO sqlalchemy.engine.Engine [raw sql] ('employees',)
# INFO:sqlalchemy.engine.Engine:[raw sql] ('employees',)
# 2024-09-14 10:29:27,587 INFO sqlalchemy.engine.Engine PRAGMA main.index_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.index_list("employees")
# 2024-09-14 10:29:27,590 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,596 INFO sqlalchemy.engine.Engine PRAGMA temp.index_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA temp.index_list("employees")
# 2024-09-14 10:29:27,608 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,612 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_info("employees")
# 2024-09-14 10:29:27,615 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,621 INFO sqlalchemy.engine.Engine PRAGMA main.index_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.index_list("employees")
# 2024-09-14 10:29:27,623 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,628 INFO sqlalchemy.engine.Engine PRAGMA temp.index_list("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA temp.index_list("employees")
# 2024-09-14 10:29:27,631 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,636 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("employees")
# INFO:sqlalchemy.engine.Engine:PRAGMA main.table_info("employees")
# 2024-09-14 10:29:27,654 INFO sqlalchemy.engine.Engine [raw sql] ()
# INFO:sqlalchemy.engine.Engine:[raw sql] ()
# 2024-09-14 10:29:27,657 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# INFO:sqlalchemy.engine.Engine:SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
# 2024-09-14 10:29:27,662 INFO sqlalchemy.engine.Engine [raw sql] ('employees',)
# INFO:sqlalchemy.engine.Engine:[raw sql] ('employees',)
# 2024-09-14 10:29:27,672 INFO sqlalchemy.engine.Engine SELECT employees.employee_id, employees.name, employees.position, employees.salary 
# FROM employees
# INFO:sqlalchemy.engine.Engine:SELECT employees.employee_id, employees.name, employees.position, employees.salary 
# FROM employees
# 2024-09-14 10:29:27,675 INFO sqlalchemy.engine.Engine [generated in 0.00381s] ()
# INFO:sqlalchemy.engine.Engine:[generated in 0.00381s] ()
# 2024-09-14 10:29:27,682 INFO sqlalchemy.engine.Engine COMMIT
# INFO:sqlalchemy.engine.Engine:COMMIT
# Updated data frame 
#    employee_id           name   position   salary
# 0            1       John Doe    Manager  50000.0
# 1            2     Jane Smith  Developer  65000.0
# 2            3  Alice Johnson   Designer  55000.0
# 3            4      Bob Brown  Developer  62000.0