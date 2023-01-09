# As a diner, I want to see the top three restaurants with the highest average food rating in a specific city so that I know where to go for good food.
import psycopg2
import sys
db, user = 'opentable', 'isdb'

SHOW_CMD = True
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

conn = psycopg2.connect(database=db, user=user)
conn.autocommit = True
cur = conn.cursor()

# print reservation table
def print_restaurant():
    query = '''
            SELECT *
              FROM Restaurants;
            '''
    cmd = cur.mogrify(query)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Restaurants:")
    print("restaurant_id | city | cuisine | restaurant_name | manager_id")
    for row in rows:
        restaurant_id,city,cuisine_type,restaurant_name,manager_id = row
        print("%s, %s, %s, %s, %s" % (restaurant_id,city,cuisine_type,restaurant_name,manager_id))

# print restaurant table
def print_review():
    query = '''
            SELECT *
              FROM Reviews;
            '''
    cmd = cur.mogrify(query)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Reviews:")
    print("review_id | score | comment | reservation_id | restaurant_id")
    for row in rows:
        review_id,food_score,comment_on_food,reservation_id,restaurant_id = row
        print("%s, %s, %s, %s, %s" % (review_id,food_score,comment_on_food,reservation_id,restaurant_id))


def get_top_restaurants(city) :
    print("US8: As a diner, I want to see the top three restaurants with the highest average food rating in a specific city so that I know where to go for good food.")
    print_restaurant()
    print()
    print_review()
    query = '''
            SELECT res.restaurant_name, sum(food_score)/count(review_id) as average
              FROM Restaurants AS res
              JOIN Reviews AS rev ON res.restaurant_id = rev.restaurant_id
             WHERE (res.city = %s)
             GROUP BY res.restaurant_name
             ORDER BY average DESC
             LIMIT 3;
            '''
    cmd = cur.mogrify(query, (city,))
    cur.execute(cmd)
    rows = cur.fetchall()
    print()
    print("top three restaurants in %s with scores: " % city)
    for row in rows:
        (name, score) = row
        print("%s, %s" % (name, score))


get_top_restaurants("pittsburgh")
