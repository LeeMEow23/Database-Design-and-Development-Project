# As a restaurant manager, I want to see the total reservations on a given day so that I can better manage staff and tables.
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
def print_reservation():
    query = '''
            SELECT *
              FROM Reservations;
            '''
    cmd = cur.mogrify(query)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Reservations:")
    print("reservation_id | date | time | people_count | restaurant_id | diner_id")
    for row in rows:
        reservation_id,reserve_date,reserve_time,number_of_people,Restaurants_restaurant_id, diner_id = row
        print("%s, %s, %s, %s, %s, %s" % (reservation_id,reserve_date,reserve_time,number_of_people,Restaurants_restaurant_id, diner_id))

# print restaurant table
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


def get_total_reservation(id, date) :
    print("US7: As a restaurant manager, I want to see the total reservations on a given day so that I can better manage staff and tables.")
    print_restaurant()
    print()
    print_reservation()
    query = '''
            SELECT count(reservation_id)
              FROM Reservations AS r
              JOIN Restaurants AS res ON r.restaurant_id = res.restaurant_id
             WHERE (res.restaurant_id = %s) and (r.reserve_date = %s);
            '''
    cmd = cur.mogrify(query, (id, date))
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        (count,) = row
        print()
        print("total reservation count for my restaurant(restaurant_id = 5) on %s: %s" % (date, count))


get_total_reservation(5, "1/1/2022")