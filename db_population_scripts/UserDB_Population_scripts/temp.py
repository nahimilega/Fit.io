import mysql.connector

db = mysql.connector.connect(user='archit', passwd='1',
                              host='localhost',
                            )




cursor = db.cursor()

## executing the statement using 'execute()' method
cursor.execute("SHOW DATABASES")



## 'fetchall()' method fetches all the rows from the last executed statement
databases = cursor.fetchall() ## it returns a list of all databases present

## printing the list of databases
print(databases)

## showing one by one database
for database in databases:
    print(database)


db.close()