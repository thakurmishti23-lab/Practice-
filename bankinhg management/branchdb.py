import mysql.connector as db
from tabulate import tabulate
con=db.connect(host="localhost",user="root",password="srishti2603",database="bank")
# if con.is_connected():
#     print("connected")
cursor=con.cursor()
def bm():
    while True:
        print('''===== BM DASHBOARD=====
        1. Check Staff
        2. Check Total Cash
        3. Total Account Holders
        4. View All Accounts
        5. View Branch Details
        6. View Fixed Deposit Summary
        7. Account / Staff Status
        8. Daily Branch Report
        9. Audit Log
        10. Logout''')

        enter=int(input("Please Enter Your Choice :- "))
        if enter==1:
            cursor.execute("select * from staff")
            a=cursor.fetchall()
            print(tabulate(a, headers=["staff_id", "branch_id", "name", "role",
                         "username", "password", "status"],tablefmt="grid"))

        elif enter==2:
            cursor.execute("select sum(balance) from accounts;") 
            b=cursor.fetchone()[0] 
            cursor.execute("select sum(closing_cash) from cashier")
            c = cursor.fetchone()[0]
            print("\nTotal Account Balance :", b)
            print("Total Closing Cash :", c)

        elif enter==3:
            cursor.execute("select count(*) from customers")

            d= cursor.fetchone()[0]

            print("\nTotal Account Holders :", d)   

        elif enter==4:
            cursor.execute("select * from accounts")
            e = cursor.fetchall()
            print(tabulate(e,headers=["account_id", "customer_id", "branch_id",
                         "account_no", "account_type", "balance",
                         "status", "opened_on"], tablefmt="grid"))

        elif enter==5:
            cursor.execute("select * from branches")
            f = cursor.fetchall()
            print(tabulate(f, headers=["branch_id", "branch_name", "branch_code",
                         "phone", "address", "status"],tablefmt="grid"))

        elif enter==6:
            cursor.execute('''select count(*), sum(amount) from fd_records ''')
            g= cursor.fetchone()
            print("\nTotal Fixed Deposits :", g[0])
            print("Total FD Amount :", g[1])

        elif enter==7:
            print("\n 1. Account Status")
            print("\n 2. Staff Status")
            status_choice = int(input("Choose an option :- "))

            if status_choice == 1:
                cursor.execute('''select account_id, account_no, status from accounts''')
                account_status = cursor.fetchall()
                print(tabulate(account_status,headers=["account_id", "account_no", "status"],tablefmt="grid" ))

            elif status_choice == 2:
                cursor.execute('''select staff_id, name, role, status from staff''')
                staff_status = cursor.fetchall()
                print(tabulate(staff_status,headers=["staff_id", "name", "role", "status"],tablefmt="grid"))


        elif enter == 8:
            print("  DAILY BRANCH REPORT  ")
            cursor.execute(''' select count(*), sum(amount) from transaction where date(transaction_time) = curdate()''')
            h = cursor.fetchone()
            print("Total Transactions :", h[0])
            print("Total Amount :", h[1])

        elif enter == 9:
            cursor.execute("select * from audit_logs")
            i = cursor.fetchall()
            print(tabulate( i , headers=["log_id", "staff_id", "customer_id", "action", "details", "timestamp"],tablefmt="grid"))

        elif enter == 10:
            print("\n Logged out successfully.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 10.")

