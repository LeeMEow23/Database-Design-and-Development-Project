\c postgres
DROP DATABASE IF EXISTS opentable;

CREATE database opentable;
\c opentable

\i create.SQL

\copy Users(user_id, fname, lname, email) FROM users.csv csv header;
\copy Diner(diner_id,total_number_reservations) FROM diner.csv csv header;
\copy OpenTable_manager(Omanager_id) FROM openTable_manager.csv csv header;
\copy Restaurant_Manager(manager_id) FROM restaurant_manager.csv csv header;
\copy Restaurants(restaurant_id, city, cuisine_type,restaurant_name, manager_id) FROM restaurants.csv csv header;
\copy Reservations(reservation_id, reserve_date, reserve_time, number_of_people, restaurant_id,diner_id) FROM reservations.csv csv header;
\copy Reviews(review_id,food_score,comment_on_food,reservation_id,restaurant_id) FROM reviews.csv csv header;
\copy Discounts(discount_id,discount_description,discount_available_date,restaurant_id) FROM discounts.csv csv header;

-- The two triggers below are used to update total_number_reservations in the Diner Table
-- One is used after insertion on reservations table
-- The other is used after deletion on reservations table

   CREATE OR REPLACE FUNCTION fn_counter() 
    RETURNS trigger
    LANGUAGE PLPGSQL AS
	$$
	BEGIN
	    UPDATE Diner
	       SET total_number_reservations = total_number_reservations+1
         WHERE diner_id = new.diner_id;
    return Null;
	END
	$$;


	DROP TRIGGER IF EXISTS tr_counter ON Reservations;
	CREATE TRIGGER tr_counter
	AFTER INSERT ON RESERVATIONS
	FOR EACH ROW
	    EXECUTE PROCEDURE fn_counter();

-- ============================================================


   CREATE OR REPLACE FUNCTION fn_counter2() 
    RETURNS trigger
    LANGUAGE PLPGSQL AS
	$$
	BEGIN
	    UPDATE Diner
	       SET total_number_reservations = total_number_reservations-1
         WHERE diner_id = old.diner_id;
    return Null;
	END
	$$;


	DROP TRIGGER IF EXISTS tr_counter2 ON Reservations;
	CREATE TRIGGER tr_counter2
	AFTER DELETE ON RESERVATIONS
	FOR EACH ROW
	    EXECUTE PROCEDURE fn_counter2();
  
  \i show_all.sql

