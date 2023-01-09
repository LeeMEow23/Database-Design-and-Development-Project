# as a diner, I want to see all the restaurants that offer discounts at a given date
# so that I can go for a cheaper meal at that given date

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
def print_discounts():
    query = '''
            SELECT *
              FROM Discounts;
            '''
    cmd = cur.mogrify(query)
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        discount_id,discount_description,discount_available_date,restaurant_id = row
        print("%s, %s, %s, %s" % (discount_id,discount_description,discount_available_date,restaurant_id))


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
        print("%s, %s, %s, %s,%s" % (restaurant_id,city,cuisine_type,restaurant_name,manager_id))



def all_reviews(discount_available_date) :
    UserStories = '# US9: As a diner, I want to see all the restaurants that offer discounts at a given date, so that I can go for a cheaper meal at that given date'
    print(UserStories)
    print()
    print("Restaurants Table:")
    print("restaurant_id | city | cuisine | restaurant_name | manager_id")
    print_restaurants()
    print()
    print("Discounts Table:")
    print("discount_id | discount_description | discount_available_date | restaurant_id")
    print_discounts()
    query = '''
            SELECT discount_description, restaurant_name
            FROM Discounts as D
            JOIN Restaurants As R on D.restaurant_id = R.restaurant_id
            WHERE discount_available_date= %s ;
            '''
    cmd = cur.mogrify(query, (discount_available_date,))
    cur.execute(cmd)
    rows = cur.fetchall()
    print()
    print("Query result: For date %s , all the restaurants that offer discounts are as following:" % (discount_available_date,))
    for row in rows:
        (discount_description, restaurant_name)= row
        print(    "%s,%s" % (discount_description, restaurant_name)  )

all_reviews("1/1/2023")
