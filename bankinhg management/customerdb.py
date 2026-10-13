import mysql.connector as db
con=db.connect(host="localhost",user="root",password="srishti2603",database="bank")
from tabulate import tabulate
# if con.is_connected():
#     print("connected")
cursor=con.cursor()
def cus():  
    while True:
        print('''=====CUSTOMERMDASHBOARD=====
        1. DepositCiew Account Details
        2. Check Balance
        3. View Transactions
        4. View Fixed Deposit
        5. Update Details
        6. Exit''')

        enter=int(input("Please Enter Your choice:- "))

        if enter==1:
            customer_id=int(input("Enter customer id:- "))
            cursor=con.cursor()
            cursor.execute("select * from customers where customer_id=%s",(customer_id,))
            a=cursor.fetchall()

            if a:
                print(tabulate(a, headers=[i[0] for i in cursor.description],tablefmt="grid"))
            else:
                print("Customer not found")

        elif enter==2:
            customer_id=int(input("Enter customer id:- "))
            cursor=con.cursor()
            cursor.execute("select balance from accounts where customer_id=%s",(customer_id,))
            a = cursor.fetchone()

            if a:
                print("Available Balance:", a[0])
            else:
                print("Account not found")

        elif enter==3:
            account_id= int(input("Enter account id:- "))
            cursor = con.cursor()
            cursor.execute("select * from transaction where account_id=%s",(account_id,))
            a = cursor.fetchall()
            if a:
                print(tabulate(a, headers=[i[0] for i in cursor.description],tablefmt="grid"))
            else:
                print("No transactions found")

        elif enter==4:
            customer_id=int(input("Enter customer id:- "))      
            cursor = con.cursor()
            cursor.execute("select customer_id, fd_type, amount, interest_rate from fd_records where customer_id=%s",(customer_id,))
            a = cursor.fetchall()
            if a:
                print(tabulate(a, headers=["customer id", "fd type", "amount","interest rate", "duration"],
                    tablefmt="grid"))
            else:
                print("No Fixed Deposit found")


        elif enter == 5:
            customer_id = int(input("Enter customer id: "))
            phone = input("Enter new phone number: ")
            address = input("Enter new address: ")
            cursor = con.cursor()
            cursor.execute("update customers set phone=%s, address=%s where customer_id=%s",(phone, address, customer_id))
            con.commit()
            print("Details updated successfully")


        elif enter == 6:
            print("Exiting Customer Dashboard...")
            break

        else:
            print("Invalid choice")     

    




