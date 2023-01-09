# as a restaurant_manager, I want to see all the food comments for my restaurant
# so that I can know where to improve in my restaurant

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

# print original Reviews table
def print_reviews():
    query = '''
            SELECT *
              FROM Reviews;
            '''
    cmd = cur.mogrify(query)
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        review_id,food_score,comment_on_food,reservation_id,restaurant_id = row
        print("%s, %s, %s, %s, %s" % (review_id,food_score,comment_on_food,reservation_id,restaurant_id))



def all_reviews(restaurant_id) :
    UserStories = '# US2: As a restaurant_manager, I want to see all the food comments for my restaurant, so that I can know where to improve in my restaurant'
    print(UserStories)
    print()
    print()
    print("Reviews Table:")
    print("review_id | score | comment | reservation_id | restaurant_id")
    print_reviews()
    query = '''
            SELECT comment_on_food
            FROM REVIEWS
            WHERE restaurant_id = %s;
            '''
    cmd = cur.mogrify(query, (restaurant_id,))
    cur.execute(cmd)
    rows = cur.fetchall()
    print()
    print("Query result: all the reviews for my restaurants(restaurant_id = 5) are:")
    for row in rows:
        (comment_on_food,)= row
        print(    "%s" % (comment_on_food,)  )

all_reviews(5)
