# as a diner, I want to see all the Mexican restaurant in pittsburgh
# so that I can pick a Mexican restaurant to visit

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
def print_restaurants():
    query = '''
            SELECT *
              FROM Restaurants;
            '''
    cmd = cur.mogrify(query)
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        restaurant_id,city,cuisine_type,restaurant_name,manager_id = row
        print("%s, %s, %s, %s, %s" % (restaurant_id,city,cuisine_type,restaurant_name,manager_id))



def all_reviews(city,cuisine_type) :
    UserStories = '# US5: As a diner, I want to see all the Mexican restaurants in pittsburgh, so that I can pick a Mexican restaurant to visit'
    print(UserStories)
    print()
    print("Restaurants Table:")
    print("restaurant_id | city | cuisine | restaurant_name | manager_id")
    print_restaurants()
    query = '''
            SELECT restaurant_name
            FROM Restaurants
            WHERE city= %s and cuisine_type = %s;
            '''
    cmd = cur.mogrify(query, (city,cuisine_type))
    cur.execute(cmd)
    rows = cur.fetchall()
    print()
    print("Query result: the required restaurants are as following:")
    for row in rows:
        (restaurant_name,)= row
        print(    "%s" % (restaurant_name,)  )

all_reviews("pittsburgh","Mexican")
