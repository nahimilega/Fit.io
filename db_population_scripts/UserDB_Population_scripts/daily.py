

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
    '''
    connection = mysql.connector.connect(user='archit', passwd='1',
                              host='localhost', database = "user"
                            )

    meal_id = 1
    for i in range(50):
        create_query_name = 'CREATE TABLE daily_record_' + str(i+1)

        table_name  = 'daily_record_' + str(i+1)
        create_data_type = """ (
                `date` DATE NOT NULL ,
                `steps` SMALLINT(7) NOT NULL,
                `cal_intake` SMALLINT(6) NOT NULL ,
                `avg_heart_rate` FLOAT(10,5) NOT NULL ,
                `sleep` SMALLINT(2) NOT NULL,
                `meal_id` SMALLINT(10) NOT NULL,
                PRIMARY KEY (`date`)
                )
                """
        create_query = create_query_name+ create_data_type
        mySql_insert_query = "INSERT INTO "+table_name +""" (date, steps, cal_intake, avg_heart_rate,sleep,meal_id)
                            VALUES (%s, %s, %s, %s, %s, %s) """





        # steps
        records_to_insert = []
        for j in range(5):
            steps = randint(0, 10000)
            claint = randint(0, 1000)
            avgHt = random.uniform(40,100)
            sleep = randint(0,24)
            to_ins = (dates[j],steps,claint,avgHt,sleep, meal_id)
            meal_id += 1
            records_to_insert.append(to_ins)




        cursor = connection.cursor()

        some = 'DROP TABLE daily_record_' + str(i+1)
        cursor.execute(some)
        connection.commit()
        cursor.execute(create_query)
        connection.commit()
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