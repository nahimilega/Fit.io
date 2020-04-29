import mysql.connector
from mysql.connector import Error


user_id = 1

try:
    '''
    connection = mysql.connector.connect(user='archit', passwd='1',
                            host='localhost', database = "user"
                        )
    '''
    connection = mysql.connector.connect(user='ug7yaayxgn0b773v', passwd='FRIWs9XAaP8PeGxjP9a2',
                        host='bfg8ldijk5ukggyco7j2-mysql.services.clever-cloud.com', database = "bfg8ldijk5ukggyco7j2"
                    )

    create_query_name = 'CREATE TABLE user_dishes'

    create_data_type = """ (
            `U_ID` INT(11) NOT NULL ,
            `dish_id` SMALLINT(7) NOT NULL,
            PRIMARY KEY (`U_ID`,`dish_id`)
            )
            """
    create_query = create_query_name + create_data_type

    cursor = connection.cursor()
    cursor.execute(create_query)
    connection.commit()

    for i in range(50):
        user_id = i+1

        get_meal_id = "select meal_id from daily_record_" + str(user_id)

        cursor = connection.cursor()
        cursor.execute(get_meal_id)
        meal_id_list = cursor.fetchall()



        to_insert = []

        for meal in meal_id_list:
            to_insert.append((user_id,meal[0]))


        mySql_insert_query = """INSERT INTO user_dishes  (U_ID, dish_id)
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
