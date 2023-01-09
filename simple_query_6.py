# As a diner, I want to book a reservation on a specific date at a specific restaurant so that I can reserve for special occasions ahead of time.
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
def print_reservations():
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
        reservation_id,reserve_date,reserve_time,number_of_people,Restaurants_restaurant_id,diner_id = row
        print("%s, %s, %s, %s, %s, %s" % (reservation_id,reserve_date,reserve_time,number_of_people,Restaurants_restaurant_id,diner_id))

def remove_reservation(resId):
    query = '''
            DELETE FROM Reservations
            WHERE Reservation_id = %s;
            '''
    cmd = cur.mogrify(query, (resId,))
    cur.execute(cmd)

def insert_into_reservation(resId,resDate,resTime,num,RestID,dinerID) :
    remove_reservation(resId)
    print("US6: As a diner, I want to book a reservation on a specific date at a specific restaurant so that I can reserve for special occasions ahead of time.")
    print_reservations()
    query = '''
            INSERT INTO Reservations
            VALUES (%s,%s,%s,%s,%s,%s);
            '''
    cmd = cur.mogrify(query, (resId,resDate,resTime,num,RestID,dinerID))
    cur.execute(cmd)
    print()
    print("--After insertion--")
    print_reservations()
    


insert_into_reservation(9, "12/12/2030", "11:11:11", 11, 4, 7)
