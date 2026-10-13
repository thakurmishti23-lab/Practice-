import mysql.connector as db
con=db.connect(host="localhost",user="root",password="srishti2603")

if con.is_connected():
    print("connected")

cursor=con.cursor()

        #CREATING DATABASE OF BANK      
cursor.execute("create database bank")
con.commit()
