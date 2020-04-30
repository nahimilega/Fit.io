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
    name =  a[temp+1][:-1] + " " + a[temp+2][:-1]
    em =  a[temp+3][:-1]
    db =  datetime.strptime(a[temp+4][:-1],"%m/%d/%Y, %H:%M:%S")
    dj =  datetime.strptime(a[temp+5][:-1], "%m/%d/%Y, %H:%M:%S")
    add =  a[temp+6][:-1]

    local = (idd,name,em,db,dj,add)
    print(idd)
    records_to_insert.append(local)
    temp += 8

#print(records_to_insert)


connection = mysql.connector.connect(user='umriv9lylxg8od0q', passwd='7bGDK5TschAyYReuDDyn',
                    host='b9uofulr45d6ajt9vnh1-mysql.services.clever-cloud.com', database = "b9uofulr45d6ajt9vnh1"
                )


create_query =  """CREATE TABLE `user` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(50) NOT NULL COLLATE 'utf8_unicode_ci',
	`email` VARCHAR(100) NOT NULL COLLATE 'utf8_unicode_ci',
	`dob` DATE NOT NULL,
	`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `address` VARCHAR(10000) NOT NULL COLLATE 'utf8_unicode_ci',
	PRIMARY KEY (`id`),
	UNIQUE INDEX `email` (`email`)
)"""

cursor = connection.cursor()
cursor.execute(create_query)


mySql_insert_query = """INSERT INTO user (id,name,email,dob,created_at,address)
                            VALUES (%s, %s, %s, %s, %s, %s) """

cursor = connection.cursor()

cursor.executemany(mySql_insert_query, records_to_insert)
connection.commit()
print(cursor.rowcount, "Record inserted successfully into Laptop table")


if (connection.is_connected()):
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
