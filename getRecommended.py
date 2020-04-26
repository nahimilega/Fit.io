import mysql.connector
from mysql.connector import Error

# Get dishes that user ate
# Get user general cal intake
# get similar dishes
# select dish with highest similarity and lowest cal difference





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




def get_user_liking_dish(user_id, Usersimilarity = 100):
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
            similarity_score =  similar_dish[2]*Usersimilarity/float(abs(float(user_meal_calInt) - float(dish_cal) )/10 + 1)
            all_potential_dishes.append((similar_dish[1],similarity_score))
        else:
            dish_cal = all_dishes[similar_dish[1]-1]
            similarity_score =  similar_dish[2]*Usersimilarity/float(abs(float(user_meal_calInt) - float(dish_cal) )/10 + 1)
            all_potential_dishes.append((similar_dish[0],similarity_score))


    selected_dishes = sorted(all_potential_dishes, key = lambda x: x[1],reverse = True)[:3]

    return selected_dishes


if __name__ == "__main__":
    user_id = 5
    meal_type = 1
    selfDishes = get_user_liking_dish(user_id)
    print(selfDishes)

    get_similar_user = "select * from user_similarity where (user_1 = {} OR user_2 = {}) AND similarity > 50.0 ".format(user_id,user_id)
    get_similar_user = executeQuery(get_similar_user)

    similar_user = []

    for userRow in get_similar_user:
        if userRow[0] == user_id:
            similar_user.append((userRow[1],userRow[2]))
        else:
            similar_user.append((userRow[0],userRow[2]))

    potential_similar_dishes = []
    for user in similar_user:
        potential_similar_dishes.extend(get_user_liking_dish(user[0],user[1]))

    potential_similar_dishes = sorted(potential_similar_dishes, key = lambda x: x[1],reverse = True)[:3]
    print(potential_similar_dishes)
    connection.close()

