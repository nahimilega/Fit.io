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

    create_query = 'CREATE TABLE dish_similarity'
    create_data_type = """ (
        `dish_1` SMALLINT(10) NOT NULL ,
        `dish_2` SMALLINT(10) NOT NULL,
        `similarity` FLOAT(5,2),
        PRIMARY KEY (`dish_1`, `dish_2`)
        )
        """
    create_query += create_data_type


    mySql_insert_query = """INSERT INTO dish_similarity  (dish_1, dish_2, similarity)
                            VALUES (%s, %s, %s) """
    to_insert = []

    for i in range(50):
        for j in range(i+1,50):
            similarity = random.uniform(0,100)
            if similarity > 50:
                to_insert.append((i+1,j+1,similarity))


    cursor = connection.cursor()
    cursor.execute(create_query)
    connection.commit()
    cursor.executemany(mySql_insert_query, to_insert)
    connection.commit()

except mysql.connector.Error as error:

    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")