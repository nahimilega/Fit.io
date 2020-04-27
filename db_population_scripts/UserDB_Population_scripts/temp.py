import mysql.connector
import datetime

db = mysql.connector.connect(user='archit', passwd='1', database = 'user',
                              host='localhost',
                            )




cursor = db.cursor()

## executing the statement using 'execute()' method
d2 = datetime.date(2020, 4, 20)
toadd = d2.strftime("%Y-%m-%d")
query = "select * from daily_record_5 where date = '{}'".format(toadd)
## 'fetchall()' method fetches all the rows from the last executed statement
cursor.execute(query)
databases = cursor.fetchall() ## it returns a list of all databases present

d1 = databases[0][0]


print(d1)
print(d2)

if d1 ==  d2:
  print("yes")
## printing the list of databases
print(databases)

## showing one by one database


db.close()