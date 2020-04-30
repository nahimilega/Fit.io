

from random import randint
import random
from datetime import datetime

'''
now = datetime.now() # current date and time
day = int(now.strftime("%d"))

for i in range(5):
    date_time = now.strftime("%Y/%m/")
    date_time += str(day)
    print(date_time)
    day = day - 1

# steps

for i in range(5):
    steps = randint(0, 10000)
    claint = randint(0, 1000)
    avgHt = random.uniform(40,100)
    sleep = randint(0,24)
    print(sleep,claint,avgHt,sleep)
'''


import mysql.connector
from mysql.connector import Error


now = datetime.now() # current date and time
day = int(now.strftime("%d"))
dates = []
for i in range(5):
    date_time = now.strftime("%Y/%m/")
    date_time += str(day)
    dates.append(date_time)
    day = day - 1

try:
    '''
    connection = mysql.connector.connect(user='ug7yaayxgn0b773v', passwd='FRIWs9XAaP8PeGxjP9a2',
                              host='bfg8ldijk5ukggyco7j2-mysql.services.clever-cloud.com', database = "bfg8ldijk5ukggyco7j2"
                            )
    SELECT concat('DROP TABLE ',TABLE_NAME ,";") as data FROM INFORMATION_SCHEMA.TABLES  WHERE TABLE_NAME LIKE 'daily_record%';

    connection = mysql.connector.connect(user='archit', passwd='1',
                              host='localhost', database = "user"
                            )
    '''
    connection = mysql.connector.connect(user='umriv9lylxg8od0q', passwd='7bGDK5TschAyYReuDDyn',
                        host='b9uofulr45d6ajt9vnh1-mysql.services.clever-cloud.com', database = "b9uofulr45d6ajt9vnh1"
                    )

    create_query_name = 'CREATE TABLE userexercise'


    create_data_type = """ (
            `uid` int,
            `datetime_e` DATE NOT NULL ,
            `steps_taken` SMALLINT(7) NOT NULL,
            `calories_burnt` SMALLINT(6) NOT NULL ,
            `avg_heart_rate` FLOAT(10,5) NOT NULL ,
            `sleep` SMALLINT(2) NOT NULL,
            PRIMARY KEY (`datetime_e`, `uid`)
            )
            """

    create_query = create_query_name+ create_data_type
    cursor = connection.cursor()
    cursor.execute(create_query)
    connection.commit()

    mySql_insert_query = """INSERT INTO userexercise (uid, datetime_e, steps_taken, calories_burnt, avg_heart_rate,sleep)
                        VALUES (%s, %s, %s, %s, %s, %s) """

    records_to_insert = []
    for i in range(50):

        # steps

        for j in range(5):
            uid = i+1
            steps = randint(0, 10000)
            claint = randint(0, 1000)
            avgHt = random.uniform(40,100)
            sleep = randint(0,24)
            to_ins = (uid,dates[j],steps,claint,avgHt,sleep)
            records_to_insert.append(to_ins)




    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")


except mysql.connector.Error as error:
    print(records_to_insert)
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")