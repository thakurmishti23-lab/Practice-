import mysql.connector as db
con=db.connect(host="localhost",user="root",password="srishti2603",database="bank")
from tabulate import tabulate
# if con.is_connected():
#     print("connected")
cursor=con.cursor()
def csh():
    while True:
        print('''===== CASHIER DASHBOARD =====
        1. Deposit Money
        2. Withdraw Money
        3. Check Balance
        4. Exit''')
    
        enter = int(input("choose an option:- "))
    
        if enter == 1:
            account_no = input("Enter account number:- ")
            amount = float(input("Enter deposit amount:- "))
            cursor = con.cursor()
            cursor.execute("update accounts set balance = balance + %s where account_no = %s",(amount, account_no))
            con.commit()
            print("Your money deposited successfully")
    
        elif enter == 2:
            account_no = input("Enter account number:- ")
            amount = float(input("Enter withdrawal amount:- "))
            cursor= con.cursor()
            cursor.execute("update accounts set balance = balance - %s where account_no = %s",(amount, account_no))
            con.commit()
            print("Your money withdrawn successfully")
    
        elif enter == 3:
            account_no = input("Enter account number:- ")
            cursor = con.cursor()
            cursor.execute("select balance from accounts where account_no = %s",(account_no,))
            a = cursor.fetchone()
            if a:
                print("balance:", a[0])
            else:
                print("Account not found")    
    
    
        elif enter== 4:
            print("Thankyouuu for visting our site sir/ma'am")
            break
        else:
            print("Invalid choice")