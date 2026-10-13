import mysql.connector as db
con=db.connect(host="localhost",user="root",password="srishti2603",database="data")
if con.is_connected():
        print("connected")
cursor=con.cursor()
cursor.execute("select * from employees")
rd=cursor.fetchall()
print(rd)
