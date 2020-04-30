import mysql.connector
from mysql.connector import Error
import random

user_id = 1

try:
    '''
    connection = mysql.connector.connect(user='archit', passwd='1',
                            host='localhost', database = "user"
                        )
    '''
    connection = mysql.connector.connect(user='umriv9lylxg8od0q', passwd='7bGDK5TschAyYReuDDyn',
                        host='b9uofulr45d6ajt9vnh1-mysql.services.clever-cloud.com', database = "b9uofulr45d6ajt9vnh1"
                    )

    create_query_name = 'CREATE TABLE eaten_food'

    create_data_type = """ (
            `uid` INT(11) NOT NULL ,
            `fid` SMALLINT(10) NOT NULL,
            PRIMARY KEY (`uid`,`fid`)
            )
            """
    create_query = create_query_name + create_data_type

    cursor = connection.cursor()
    cursor.execute(create_query)
    connection.commit()

    for i in range(50):
        user_id = i+1


        to_insert = []
        for meal in random.sample(range(1, 50), 9):
            to_insert.append((user_id,meal))


        mySql_insert_query = """INSERT INTO eaten_food  (uid, fid)
                                VALUES (%s, %s) """

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, to_insert)
        connection.commit()

except mysql.connector.Error as error:

    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
