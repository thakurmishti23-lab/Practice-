import mysql.connector as db
con = db.connect(host="localhost", user="root", password="srishti2603", database="bank")
from tabulate import tabulate
# if con.is_connected():
#     print("connected")
cursor = con.cursor()
def fd():
    while True:
        print('''=====FIXED DEPOSIT DASHBOARD=====
        1. Create Fixed Deposit
        2. View Fixed Deposit
        3. Update Fixed Deposit
        4. Exit''')

        enter = int(input("choose an option: "))

        if enter == 1:
            customer_id = int(input("Enter customer id:- "))
            fd_type = input("Enter FD type:- ")
            amount = float(input("Enter FD amount:- "))
            interest_rate = float(input("Enter interest rate:- "))
            cursor = con.cursor()
            cursor.execute("insert into fd_records(customer_id, fd_type, amount, interest_rate) values(%s,%s,%s,%s)",(customer_id, fd_type, amount, interest_rate))
            con.commit()
            print("Fixed Deposit created successfully")

        elif enter == 2:
            customer_id = int(input("Enter customer id:- "))
            cursor = con.cursor()
            cursor.execute("select customer_id, fd_type, amount, interest_rate from fd_records where customer_id=%s",(customer_id,))
            a = cursor.fetchall()
            if a:
                print(tabulate(a, headers=["customer id", "fd type", "amount", "interest rate"],tablefmt="grid"))
            else:
                print("No Fixed Deposit found")

        elif enter == 3:
            customer_id = int(input("Enter customer id:- "))
            amount = float(input("Enter new FD amount:- "))
            cursor = con.cursor()
            cursor.execute( "update fd_records set amount=%s where customer_id=%s",(amount, customer_id))
            con.commit()
            print("Fixed Deposit updated successfully")

        elif enter == 4:
            print("Exiting Fixed Deposit Dashboard...")
            break

        else:
            print("Invalid choice")
