from random import randint
import random
from datetime import datetime
import mysql.connector
from mysql.connector import Error





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



    connection2 = mysql.connector.connect(user='up7wlunkxcruzlb2', passwd='mB9DEDRo2fTIQpua0pfD',
                              host='b6ozuvhquh16mibwxlqc-mysql.services.clever-cloud.com', database = "b6ozuvhquh16mibwxlqc"
                            )
    cursor2 = connection2.cursor()
    cursor2.execute("Select Calorie from Food")
    dish_info = cursor2.fetchall()
    print(dish_info)
    create_query = 'CREATE TABLE meals'
    create_data_type = """ (
            `meal_id` SMALLINT(10) NOT NULL ,
            `meal_type` SMALLINT(1) NOT NULL,
            `meal_items` VARCHAR(200),
            `cal_intake` SMALLINT(6) NOT NULL ,
            PRIMARY KEY (`meal_id`, `meal_type`)
            )
            """
    # 0 for breakfast 1 for lunch 2 for snacks 3 for dinner
    create_query += create_data_type
    toadd = []
    mySql_insert_query = """INSERT INTO meals  (meal_id, meal_type, meal_items, cal_intake)
                            VALUES (%s, %s, %s, %s) """

    for i in range(250):
        for j in range(4):
            dish = randint(1,50)
            to_ins = (i+1, j,dish ,dish_info[dish-1][0])
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