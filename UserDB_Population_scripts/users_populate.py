from datetime import datetime
import mysql.connector
from mysql.connector import Error
records_to_insert = []

count = 0
# open file and read the content in a list
f = open('data.txt', 'r')
a = f.readlines()

temp = 0
while temp<len(a):


    idd =  int(a[temp][:-1])
    fn =  a[temp+1][:-1]
    ln =  a[temp+2][:-1]
    em =  a[temp+3][:-1]
    db =  datetime.strptime(a[temp+4][:-1],"%m/%d/%Y, %H:%M:%S")
    dj =  datetime.strptime(a[temp+5][:-1], "%m/%d/%Y, %H:%M:%S")
    add =  a[temp+6][:-1]
    con =  a[temp+7][:-1]

    local = (idd,fn,ln,em,db,dj,add,con)
    print(idd)
    records_to_insert.append(local)
    temp += 8

#print(records_to_insert)


connection = mysql.connector.connect(host="localhost",
    user="root",
    passwd="scorpio",
    database="testing"
)


create_query =  """CREATE TABLE `users` (
	`U_ID` INT(11) NOT NULL AUTO_INCREMENT,
	`first_name` VARCHAR(50) NOT NULL COLLATE 'utf8_unicode_ci',
	`last_name` VARCHAR(50) NOT NULL COLLATE 'utf8_unicode_ci',
	`email` VARCHAR(100) NOT NULL COLLATE 'utf8_unicode_ci',
	`date_of_birth` DATE NOT NULL,
	`added_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `address` VARCHAR(10000) NOT NULL COLLATE 'utf8_unicode_ci',
        `contact` VARCHAR(20) NOT NULL COLLATE 'utf8_unicode_ci',
	PRIMARY KEY (`U_ID`),
	UNIQUE INDEX `email` (`email`)
)"""
cursor = connection.cursor()
cursor.execute(create_query)


mySql_insert_query = """INSERT INTO users (U_ID,first_name,last_name,email,date_of_birth,added_on,address,contact)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

cursor = connection.cursor()

cursor.executemany(mySql_insert_query, records_to_insert)
connection.commit()
print(cursor.rowcount, "Record inserted successfully into Laptop table")


if (connection.is_connected()):
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
