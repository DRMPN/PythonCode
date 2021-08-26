-- Keep a log of any SQL queries you execute as you solve the mystery.

/*
Your goal is to identify:

Who the thief is,
What city the thief escaped to, and
Who the thief’s accomplice is who helped them escape

All you know is that the theft
took place on July 28, 2020 and that it
took place on Chamberlin Street.

*/

-- general information
SELECT id, description
FROM crime_scene_reports
WHERE street = "Chamberlin Street" AND month = 7 AND day = 28;
-- Result: 10:15am at courthouse three witnesses

-- information from witnesses:
SELECT *
FROM interviews
WHERE month = 7 AND day = 28
ORDER BY id DESC
LIMIT 3;
-- Results:
-- Raymond
-- As the thief was leaving the courthouse, they called someone who talked to them for less than a minute.
SELECT DISTINCT caller, receiver, duration
FROM phone_calls
WHERE month = 7 AND day = 28 AND duration < 60;
-- earliest flight out of Fiftyville tomorrow
SELECT *
FROM flights
WHERE month = 7 AND day = 28
ORDER BY destination_airport_id, day, hour;
-- asked the person on the other end of the phone to purchase the flight ticket

-- Eugene
-- Earlier this morning, I was walking by the ATM on Fifer Street and saw the thief there withdrawing some money
SELECT *
FROM atm_transactions
WHERE month = 7 AND day = 28 AND atm_location = "Fifer Street" AND transaction_type = "withdraw";

-- Ruth
-- Sometime within ten minutes of the theft, I saw the thief get into a car in the courthouse parking lot and drive away.
SELECT *
FROM courthouse_security_logs
WHERE month = 7 AND day = 28 AND hour = 10 AND minute <= 25 AND activity = "exit";



-- find thief with extracted information form above:
SELECT people.*, phone_calls.receiver
FROM people
INNER JOIN phone_calls ON people.phone_number = phone_calls.caller
INNER JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
INNER JOIN bank_accounts ON people.id = bank_accounts.person_id
INNER JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE   (phone_calls.month = 7  AND courthouse_security_logs.month = 7  AND atm_transactions.month = 7) AND
        (phone_calls.day = 28   AND courthouse_security_logs.day = 28   AND atm_transactions.day = 28)  AND
        phone_calls.duration < 60 AND
        courthouse_security_logs.activity = "exit" AND courthouse_security_logs.hour = 10 AND courthouse_security_logs.minute <= 25 AND
        atm_transactions.atm_location = "Fifer Street" AND atm_transactions.transaction_type = "withdraw" AND
        people.passport_number IN (SELECT passport_number FROM passengers INNER JOIN flights ON passengers.flight_id = flights.id WHERE month = 7 AND day = 29)
ORDER BY courthouse_security_logs.minute;
-- Ernest or Russell



-- flight information
SELECT *
FROM flights
INNER JOIN passengers ON flights.id = flight_id
WHERE passport_number IN (5773159633, 3592750733) AND day = 29;

SELECT *
FROM airports
WHERE id = 4 OR id = 6;
-- destination is london or boston



-- find accomplice
SELECT *
FROM people
WHERE phone_number IN ("(375) 555-8161", "(725) 555-3243");
-- Berthold or Philip



-- friends might get money to buy a ticket
SELECT *
FROM people
INNER JOIN bank_accounts ON people.id = bank_accounts.person_id
INNER JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE   phone_number IN ("(375) 555-8161", "(725) 555-3243") AND
        atm_transactions.month = 7 AND atm_transactions.day = 28;
-- the do not withdraw money on 28 to buy a ticket
-- but if the day is 27 or 29 then berthold deposited 55 and 90 -> recieved money from some source -> he is accomplice and the thief is ernest