import mysql.connector
import datetime
mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="library")
c=mydb.cursor()
c.execute("select * from books")
for r in c:
    print(r)
c2=mydb.cursor()
c2.execute("select * from issue")
for r in c2:
    print(r)
#To insert data from database
bid=input("Enter Book ID")
uid=input("Enter User ID")
iid=str(datetime.datetime.now())
c3=mydb.cursor()
c3.execute("insert into issue values(%s,%s,%s)",(iid,bid,uid))
mydb.commit()
print("Book issued successfully")




