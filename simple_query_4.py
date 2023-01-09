# As a restaurant manager, I want to offer discounts on a given date in my restaurant so that I can attract more customers.
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
def print_discount():
    query = '''
            SELECT *
              FROM Discounts;
            '''
    cmd = cur.mogrify(query)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Discounts:")
    print("discount_id | description | available_date | restaurant_id")
    for row in rows:
        discount_id,discount_description,discount_available_date,restaurant_id = row
        print("%s, %s, %s, %s" % (discount_id,discount_description,discount_available_date,restaurant_id))

def remove_discount(discount_id):
    query = '''
            DELETE FROM Discounts
             WHERE Discount_id = %s;
            '''
    cmd = cur.mogrify(query, (discount_id,))
    cur.execute(cmd)

def insert_into_discount(discount_id,discount_description,discount_available_date,restaurant_id):
    remove_discount(discount_id)
    print("US4: As a restaurant manager, I want to offer discounts on a given date in my restaurant so that I can attract more customers.")
    print_discount()
    query = '''
            INSERT INTO Discounts
            VALUES (%s,%s,%s,%s);
            '''
    cmd = cur.mogrify(query, (discount_id,discount_description,discount_available_date,restaurant_id))
    cur.execute(cmd)
    print()
    print("--After insertion--")
    print_discount()


insert_into_discount(6, "get a pair of free donuts!", "11/11/2022", 3)