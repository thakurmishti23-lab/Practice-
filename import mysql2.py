import mysql.connector as db

con=db.connect(host="localhost",user="root",password="srishti2603",database="data")

if con.is_connected():
    print("connected")

cursor=con.cursor()
# creating user table

cursor.execute("""create table users(
    user_id int primary key,
    name varchar(30),
    password int unique
)
""")


# inserting user value

cursor.execute("""
insert ignore into users(user_id, name, password)
values(101, 'Srishti', 1234)
""")


# creating employee table

cursor.execute("""
create table if not exists emp1(
    emp_id int primary key,
    emp_name varchar(30),
    department varchar(20)
)
""")


# inserting employee values

cursor.execute("""
insert ignore into emp1(emp_id, emp_name, department)
values
(1001, 'Prikshit', 'Cloud Computing'),
(1002, 'Sneha', 'AI&ML'),
(1003, 'Smitha', 'Data Analytics'),
(1004, 'Kushal', 'AI&ML'),
(1005, 'Sumit', 'Cloud Computing')
""")


con.commit()

print("tables created successfully")


# login work

print("\n        LOGIN PAGE")

name = input("ENTER YOUR NAME:- ")
password = int(input("ENTER YOUR PASSWORD:- "))

cursor.execute(
    "select * from users where name = %s and password = %s",
    (name, password)
)

user = cursor.fetchone()


if user:

    print("\nYou logged in successfully!!!")
    print(".....Welcome to the Employee Data.....")

    while True:

        print("\n1. SHOW ALL RECORDS")
        print("2. UPDATE RECORD")
        print("3. DELETE RECORD")
        print("4. DELETE AND RELOAD RECORDS")
        print("0. EXIT")

        choice = int(input("ENTER YOUR CHOICE:- "))


        if choice == 1:

            cursor.execute("select * from emp1")

            records = cursor.fetchall()

            for record in records:
                print(record)


        elif choice == 2:

            emp_id = int(input("ENTER EMPLOYEE ID:- "))
            department = input("ENTER NEW DEPARTMENT:- ")

            cursor.execute(
                "update emp1 set department = %s where emp_id = %s",
                (department, emp_id)
            )

            con.commit()

            print("record updated successfully")


        elif choice == 3:

            emp_id = int(input("ENTER EMPLOYEE ID:- "))

            cursor.execute(
                "delete from emp1 where emp_id = %s",
                (emp_id,)
            )

            con.commit()

            print("record deleted successfully")


        elif choice == 4:

            cursor.execute("delete from emp1")

            cursor.execute("""
            insert into emp1(emp_id, emp_name, department)
            values
            (1001, 'Prikshit', 'Cloud Computing'),
            (1002, 'Sneha', 'AI&ML'),
            (1003, 'Smitha', 'Data Analytics'),
            (1004, 'Kushal', 'AI&ML'),
            (1005, 'Sumit', 'Cloud Computing')
            """)

            con.commit()

            print("records deleted and reloaded successfully")


        elif choice == 0:

            print("thank you")
            break


        else:

            print("invalid choice")


else:

    print("wrong name or password")


cursor.close()
con.close()