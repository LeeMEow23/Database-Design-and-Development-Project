# As a OpenTable manager,  I want to see how many restaurants in total are using our website so that I can make better business decisions.
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


def get_total_restaurants() :
    print("US1: As a OpenTable manager,  I want to see how many restaurants in total are using our website so that I can make better business decisions.")
    print_restaurant()
    query = '''
            SELECT count(restaurant_id)
              FROM Restaurants;
            '''
    cmd = cur.mogrify(query)
    cur.execute(cmd)
    rows = cur.fetchall()
    print()
    print("total number of restaurants:")
    for row in rows:
        (count) = row
        print("%s" % count)


get_total_restaurants()
