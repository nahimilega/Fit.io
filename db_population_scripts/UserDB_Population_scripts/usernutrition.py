from random import randint
import random
from datetime import datetime
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

    connection2 = mysql.connector.connect(user='up7wlunkxcruzlb2', passwd='mB9DEDRo2fTIQpua0pfD',
                              host='b6ozuvhquh16mibwxlqc-mysql.services.clever-cloud.com', database = "b6ozuvhquh16mibwxlqc"
                            )



    cursor2 = connection2.cursor()
    cursor2.execute("Select Name, Calorie from Food")
    dish_info = cursor2.fetchall()
    create_query = 'CREATE TABLE usernutrition'
    create_data_type = """ (
            `uid` INT NOT NULL ,
            `datetime_e` DATE NOT NULL ,
            `foodtype` SMALLINT(1) NOT NULL,
            `food_consumed` VARCHAR(200) NOT NULL,
            `calories_consumed` SMALLINT(6) NOT NULL ,
            PRIMARY KEY (`uid`, `datetime_e`, `foodtype`)
            )
            """
    # 0 for breakfast 1 for lunch 2 for snacks 3 for dinner
    create_query += create_data_type
    toadd = []
    mySql_insert_query = """INSERT INTO usernutrition  (uid, datetime_e, foodtype, food_consumed, calories_consumed)
                            VALUES (%s, %s, %s, %s, %s) """

    for i in range(50):
        for m in range(5):
            datet = dates[m]
            for j in range(4):
                dish = randint(1,50)
                to_ins = (i+1,datet, j, dish_info[dish-1][0] ,dish_info[dish-1][1])
                toadd.append(to_ins)



    print(toadd[0])
    cursor = connection.cursor()
    cursor.execute(create_query)
    connection.commit()
    cursor.executemany(mySql_insert_query, toadd)
    connection.commit()

except mysql.connector.Error as error:

    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        cursor2.close()
        connection2.close()
        print("MySQL connection is closed")