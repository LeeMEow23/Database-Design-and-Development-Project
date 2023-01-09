-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-12-05 00:26:20.718

-- tables
-- Table: Diner
CREATE TABLE Diner (
    diner_id int  NOT NULL,
    total_number_reservations int  NOT NULL,
    CONSTRAINT Diner_pk PRIMARY KEY (diner_id)
);

-- Table: Discounts
CREATE TABLE Discounts (
    discount_id int  NOT NULL,
    discount_description text  NOT NULL,
    discount_available_date date  NOT NULL,
    restaurant_id int  NOT NULL,
    CONSTRAINT Discounts_pk PRIMARY KEY (discount_id)
);

-- Table: OpenTable_manager
CREATE TABLE OpenTable_manager (
    Omanager_id int  NOT NULL,
    CONSTRAINT OpenTable_manager_pk PRIMARY KEY (Omanager_id)
);

-- Table: Reservations
CREATE TABLE Reservations (
    reservation_id int  NOT NULL,
    reserve_date date  NOT NULL,
    reserve_time time  NOT NULL,
    number_of_people int  NOT NULL,
    restaurant_id int  NOT NULL,
    diner_id int  NOT NULL,
    CONSTRAINT Reservations_pk PRIMARY KEY (reservation_id)
);

-- Table: Restaurant_Manager
CREATE TABLE Restaurant_Manager (
    manager_id int  NOT NULL,
    CONSTRAINT Restaurant_Manager_pk PRIMARY KEY (manager_id)
);

-- Table: Restaurants
CREATE TABLE Restaurants (
    restaurant_id int  NOT NULL,
    city text  NOT NULL,
    cuisine_type text  NOT NULL,
    restaurant_name text  NOT NULL,
    manager_id int  NOT NULL,
    CONSTRAINT Restaurants_pk PRIMARY KEY (restaurant_id)
);

-- Table: Reviews
CREATE TABLE Reviews (
    review_id int  NOT NULL,
    food_score int  NOT NULL,
    comment_on_food text  NOT NULL,
    reservation_id int  NOT NULL,
    restaurant_id int  NOT NULL,
    CONSTRAINT Reviews_pk PRIMARY KEY (review_id)
);

-- Table: Users
CREATE TABLE Users (
    user_id int  NOT NULL,
    fname text  NOT NULL,
    lname text  NOT NULL,
    email text  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (user_id)
);

-- foreign keys
-- Reference: Customer_Users (table: Diner)
ALTER TABLE Diner ADD CONSTRAINT Customer_Users
    FOREIGN KEY (diner_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Discounts_Restaurants (table: Discounts)
ALTER TABLE Discounts ADD CONSTRAINT Discounts_Restaurants
    FOREIGN KEY (restaurant_id)
    REFERENCES Restaurants (restaurant_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: OpenTable_manager_Users (table: OpenTable_manager)
ALTER TABLE OpenTable_manager ADD CONSTRAINT OpenTable_manager_Users
    FOREIGN KEY (Omanager_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reservations_Diner (table: Reservations)
ALTER TABLE Reservations ADD CONSTRAINT Reservations_Diner
    FOREIGN KEY (diner_id)
    REFERENCES Diner (diner_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reservations_Restaurants (table: Reservations)
ALTER TABLE Reservations ADD CONSTRAINT Reservations_Restaurants
    FOREIGN KEY (restaurant_id)
    REFERENCES Restaurants (restaurant_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Restaurant_Manager_Users (table: Restaurant_Manager)
ALTER TABLE Restaurant_Manager ADD CONSTRAINT Restaurant_Manager_Users
    FOREIGN KEY (manager_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Restaurants_Restaurant_Manager (table: Restaurants)
ALTER TABLE Restaurants ADD CONSTRAINT Restaurants_Restaurant_Manager
    FOREIGN KEY (manager_id)
    REFERENCES Restaurant_Manager (manager_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reviews_Reservations (table: Reviews)
ALTER TABLE Reviews ADD CONSTRAINT Reviews_Reservations
    FOREIGN KEY (reservation_id)
    REFERENCES Reservations (reservation_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reviews_Restaurants (table: Reviews)
ALTER TABLE Reviews ADD CONSTRAINT Reviews_Restaurants
    FOREIGN KEY (restaurant_id)
    REFERENCES Restaurants (restaurant_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

