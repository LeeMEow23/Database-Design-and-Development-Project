# as a OpenTable Manager, I want to see the customers who have made the most reservations using our website
# so that I can email them and give them cash back bonus
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
def print_reservations():
    query = '''
            SELECT *
              FROM reservations;
            '''
    cmd = cur.mogrify(query)
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        reservation_id,reserve_date,reserve_time,number_of_people,Restaurants_restaurant_id,diner_id = row
        print("%s, %s, %s, %s,%s,%s" % (reservation_id,reserve_date,reserve_time,number_of_people,Restaurants_restaurant_id,diner_id))


# print original Reviews table
def print_diner():
    query = '''
            SELECT *
              FROM Diner;
            '''
    cmd = cur.mogrify(query)
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        diner_id,total_number_reservations = row
        print("%s, %s" % (diner_id,total_number_reservations))


def test_trigger(delete_num,reservation_id,reserve_date,reserve_time,number_of_people,Restaurants_restaurant_id,diner_id):
##def test_trigger(delete_num):
    UserStories = '# US10: as a OpenTable Manager, I want to see the customers who have made the most reservations using our website,so that I can email them and give them cash back bonus'
    print(UserStories)
    print()

    test_prep= '''
    DELETE FROM Reservations
    WHERE reservation_id = %s;
    '''
    cmd = cur.mogrify(test_prep,(delete_num,))
    cur.execute(cmd)

    print("Reservations Table Before:")
    print("reservation_id | date | time | people_count | restaurant_id | diner_id")
    print_reservations()
    print()

    print("Diner Table Before:")
    print("diner_id | total_reservations")
    print_diner()
    print()

    query = '''
    INSERT INTO RESERVATIONS
    VALUES (%s,%s,%s,%s,%s,%s);
    '''
    cmd = cur.mogrify(query, (reservation_id,reserve_date,reserve_time,number_of_people,Restaurants_restaurant_id,diner_id))
    cur.execute(cmd)
    
    print("Reservations Table After INSERTION:")
    print("reservation_id | date | time | people_count | restaurant_id | diner_id")
    print_reservations()
    print()
    print("Diner Table After INSERTION:")
    print("diner_id | total_reservations")
    print_diner()
    print()

    query2 = '''
    SELECT diner_id,fname,lname,email
    FROM diner as D1
    JOIN users 
    ON D1.diner_id = user_id
    WHERE D1.total_number_reservations = (SELECT max(D2.total_number_reservations) 
                                            FROM diner as D2 )
    '''
    cmd = cur.mogrify(query2)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("The top customers who book the most are following:")
    for row in rows:
        (diner_id,fname,lname,email)= row
        print(    "%s,%s,%s,%s" % (diner_id,fname,lname,email)  )

test_trigger(9,9,"1/1/2023/","12:12:13",4,3,7)

