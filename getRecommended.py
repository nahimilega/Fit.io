import mysql.connector
from mysql.connector import Error

# Get dishes that user ate
# Get user general cal intake
# get similar dishes
# select dish with highest similarity and lowest cal difference


user_id = 5
meal_type = 1


connection = mysql.connector.connect(user='archit', passwd='1',
                        host='localhost', database = "user"
                    )


def sanatizeList(input_list):
    temp = []
    for i in input_list:
        temp.append(i[0])
    return temp



def executeQuery(query):
    cursor = connection.cursor()
    cursor.execute(query)
    temp =  cursor.fetchall()
    cursor.close()
    return temp






get_user_dishes = "select dish_id from user_dishes where U_ID = " + str(user_id)
get_user_dishes = executeQuery(get_user_dishes)


valid_meals = "select meal_id from daily_record_" + str(user_id)
valid_meals = tuple(sanatizeList(executeQuery(valid_meals)))

user_meal_calInt = """SELECT AVG(cal_intake) AS average
                    FROM meals
                    WHERE meal_type = """ + str(meal_type) + " and meal_id in (select meal_id from daily_record_"+ str(user_id)+")"

user_meal_calInt = executeQuery(user_meal_calInt)[0][0]

get_user_dishes = sanatizeList(get_user_dishes)

t = tuple(get_user_dishes)
similar_dishes = "SELECT * from dish_similarity where dish_1 IN {} OR dish_2 IN {}".format(t,t)
similar_dishes = executeQuery(similar_dishes)
all_dishes = "SELECT Calorie from Food"
all_dishes = sanatizeList(executeQuery(all_dishes))

all_potential_dishes = []
similarity_score = []
for similar_dish in similar_dishes:

    if similar_dish[0] in get_user_dishes:
        dish_cal = all_dishes[similar_dish[1]-1]
        similarity_score =  similar_dish[2]/float(abs(float(user_meal_calInt) - float(dish_cal) ) + 1)
        all_potential_dishes.append((similar_dish[1],similarity_score))

    else:
        dish_cal = all_dishes[similar_dish[1]-1]
        similarity_score =  similar_dish[2]/float(abs(float(user_meal_calInt) - float(dish_cal) ) + 1)
        all_potential_dishes.append((similar_dish[0],similarity_score))


selected_dishes = sorted(all_potential_dishes, key = lambda x: x[1],reverse = True)[:3]

print(selected_dishes)


connection.close()

