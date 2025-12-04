-- This code creates an SQL table that matches the Documentation provided on the task.
-- The ID Autoincrements for no repeats.
-- And all data is filled out

-- CREATE TABLE RestaurantReservations(ReservationID INTEGER PRIMARY KEY AUTOINCREMENT,
--                                     UserName TEXT NOT NULL,
--                                     UserEmail TEXT NOT NULL,
--                                     ReservationDate DATE NOT NULL,
--                                     Time TIME NOT NULL,
--                                     NumberOfGuests INTEGER NOT NULL
-- );

-- INSERT INTO RestaurantReservations(UserName, UserEmail, ReservationDate, Time, NumberOfGuests) VALUES
--     ('Alice', 'alice@example.com', '2024-09-20', '19:00', 4),
--     ('Bob', 'bob@example.com', '2024-09-27', '20:30', 2),
--     ('Charlie', 'charlie@example.com', '2024-09-13', '18:45', 3),
--     ('Diana', 'diana@example.com', '2024-09-06', '19:30', 5),
--     ('Ethan', 'ethan@example.com', '2024-09-13', '21:00', 2);

-- This code selects every entry into the RestaurantReservations table where Time starts with "19:"
-- this lets us get anything from 19:00 to 19:59 (The only valid records but would accept "19:aa" etc..)
-- OR Time = "20:00" allows us to finish the query by making it fully inclusive
--
-- SELECT * FROM RestaurantReservations WHERE Time LIKE "19:%" OR Time = "20:00";


-- This code adds up the "NumberOfGuests" Column (then saves into a variable known as "TotalGuests")
-- For Every single entry into the RestaurantReservations Table, where the dates are between '2024-09-13' and '2024-09-25'
-- It is an inclusive between and spits out the correct answer of 9

SELECT SUM(NumberOfGuests) as TotalGuests
FROM RestaurantReservations
WHERE ReservationDate BETWEEN '2024-09-13' AND '2024-09-25';


