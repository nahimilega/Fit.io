# TINYINT(1)
from random import randint
import random
disease = ['heart disease', 'cancer','skin disease', 'bone disease']

import mysql.connector
from mysql.connector import Error

from random import randint
import random
from datetime import datetime




try:
    '''
    connection = mysql.connector.connect(user='archit', passwd='1',
                              host='localhost', database = "test"
                            )
    '''
    connection = mysql.connector.connect(user='ug7yaayxgn0b773v', passwd='FRIWs9XAaP8PeGxjP9a2',
                            host='bfg8ldijk5ukggyco7j2-mysql.services.clever-cloud.com', database = "bfg8ldijk5ukggyco7j2"
                        )



    create_query =     """CREATE TABLE `at_risk` (
	`U_ID` INT(11) NOT NULL AUTO_INCREMENT,
	`at_risk` TINYINT(1) NOT NULL,
	`disease`VARCHAR(200) NOT NULL,
	PRIMARY KEY (`U_ID`,`disease`)
        )"""
    cursor = connection.cursor()
    cursor.execute(create_query)
    j = 1
    for i in range(20):
        mySql_insert_query = """INSERT INTO at_risk (U_ID,disease,at_risk)
                            VALUES (%s, %s, %s) """

        # steps
        records_to_insert = []
        atridk = randint(0, 1)
        atridk2 = randint(0, 1)
        a,b = random.sample(range(0, 3), 2)

        c = (j, disease[a], atridk)
        cc = (j, disease[b], atridk2)
        records_to_insert.append(c)
        records_to_insert.append(cc)
        inc = randint(1, 3)
        j+= inc

        cursor = connection.cursor()

        cursor.executemany(mySql_insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")


except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")