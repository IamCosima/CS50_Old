-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT description from crime_scene_reports
Where month = 7 AND day = 28 AND street = "Humphrey Street";
-- Answear Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
--Littering took place at 16:36. No known witnesses.

SELECT transcript,name from interviews
Where month = 7 AND day = 28 AND year = 2021;

--Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
--If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot
--in that time frame.	Ruth	7	28	2021
--I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived
--at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.	Eugene	7	28	2021
--As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
 --In the call, I heard the thief say that they were planning to take the earliest flight out
 --of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ...	Raymond	7	28	2021

SELECT account_number FROM "atm_transactions" WHERE atm_location = "Leggett Street"AND transaction_type = "deposit" AND month = 7 AND day = 28 AND year = 2021;
--account num = 86363979

SELECT account_number FROM "atm_transactions" WHERE atm_location = "Leggett Street"AND transaction_type = "withdraw" AND month = 7 AND day = 28 AND year = 2021;
--account_number
--28500762
--28296815
--76054385
--49610011
--16153065
--25506511
--81061156
--26013199

SELECT person_id FROM "bank_accounts" WHERE account_number = 86363979;
--person_id
--948985 Kaelyn
SELECT person_id FROM "bank_accounts" WHERE account_number = 28500762;
--person_id
--467400 Luca
SELECT person_id FROM "bank_accounts" WHERE account_number = 28296815;
--person_id
--395717 Kenny
SELECT person_id FROM "bank_accounts" WHERE account_number = 76054385;
--person_id
--449774 Taylor
SELECT person_id FROM "bank_accounts" WHERE account_number = 49610011;
--person_id
--686048 Bruce
SELECT person_id FROM "bank_accounts" WHERE account_number = 16153065;
--person_id
--458378 Brooke
SELECT person_id FROM "bank_accounts" WHERE account_number = 25506511;
--person_id
--396669 Iman
SELECT person_id FROM "bank_accounts" WHERE account_number = 81061156;
--person_id
--438727 Benista
SELECT person_id FROM "bank_accounts" WHERE account_number = 26013199;
--person_id
--514354 Diana

SELECT name FROM "people" WHERE id = 467400;
--Luca
SELECT name FROM "people" WHERE id = 395717;
--Kenny
SELECT name FROM "people" WHERE id = 449774;
--Taylor
SELECT name FROM "people" WHERE id = 686048;
--Bruce
SELECT name FROM "people" WHERE id = 458378;
--Brooke
SELECT name FROM "people" WHERE id = 396669;
--Iman
SELECT name FROM "people" WHERE id = 438727;
--Benista
SELECT name FROM "people" WHERE id = 514354;
--Diana


 SELECT Activity,license_plate FROM bakery_security_logs
Where month = 7 AND day = 28 AND year = 2021 AND hour = 10 AND minute < 25;
--exit	5P2BI95 Vanessa
--exit	94KL13X Bruce --
--exit	6P58WS2 Barry
--exit	4328GD8 Luca --
--exit	G412CB7 Sofia
--exit	L93JTIZ Iman --
--exit	322W7JE Diana --
--exit	0NTHK55 Kelsey



SELECT id,HOUR, minute FROM "flights" WHERE origin_airport_id = 8 AND day = 28 AND month = 7 AND year = 2021;
--id	hour	minute
--6	13	49


SELECT passport_number FROM "passengers" WHERE flight_id = 6;
--passport_number
--3835860232
--1618186613
--7179245843
--1682575122
--7597790505
--6128131458
--6264773605
--3642612721

SELECT name FROM "people" WHERE id = 948985;
--name
--Kaelyn

SELECT name,passport_number,phone_number,license_plate FROM "people" WHERE id = 948985;
--name	passport_number	phone_number	license_plate
--Kaelyn	8304650265	(098) 555-1164	I449449


--Suspects

--Diana -- 514354 bank_accounts
SELECT name,passport_number,phone_number,license_plate FROM "people" WHERE id = 514354;
--name	passport_number	phone_number	license_plate
--Diana	3592750733	(770) 555-1861	322W7JE
SELECT receiver,duration FROM "phone_calls" WHERE month = 7 AND day = 28 AND year = 2021 AND caller = "(770) 555-1861" ;
--receiver	duration
--(725) 555-3243	49

SELECT name,passport_number FROM "people" WHERE phone_number = "(725) 555-3243" ;
--name	passport_number
--Philip	3391710505

--Iman -- 396669 bank_accounts
SELECT name,passport_number,phone_number,license_plate FROM "people" WHERE id = 396669;
--name	passport_number	phone_number	license_plate
--Iman	7049073643	(829) 555-5269	L93JTIZ

SELECT receiver,duration FROM "phone_calls" WHERE month = 7 AND day = 28 AND year = 2021 AND caller = "(829) 555-5269" ;
--Nothing

--Luca -- 467400 bank_accounts
SELECT name,passport_number,phone_number,license_plate FROM "people" WHERE id = 467400;
--name	passport_number	phone_number	license_plate
--Luca	8496433585	(389) 555-5198	4328GD8

SELECT receiver,duration FROM "phone_calls" WHERE month = 7 AND day = 28 AND year = 2021 AND caller = "(389) 555-5198" ;
--nothing

--Bruce -- 686048 bank_accounts
SELECT name,passport_number,phone_number,license_plate FROM "people" WHERE id = 686048;
--name	passport_number	phone_number	license_plate
--Bruce	5773159633	(367) 555-5533	94KL13X

SELECT receiver,duration FROM "phone_calls" WHERE month = 7 AND day = 28 AND year = 2021 AND caller = "(367) 555-5533" ;
receiver	duration
--(375) 555-8161	45
--(344) 555-9601	120
--(022) 555-4052	241
--(704) 555-5790	75

SELECT name,passport_number FROM "people" WHERE phone_number = "(375) 555-8161" ;
--name	passport_number
--Robin	NULL



SELECT caller,receiver,duration FROM "phone_calls" WHERE month = 7 AND day = 28 AND year = 2021 AND duration <60;
--caller	receiver	duration
--(130) 555-0289	(996) 555-8899	51
--(499) 555-9472	(892) 555-8872	36
--(367) 555-5533	(375) 555-8161	45
--(499) 555-9472	(717) 555-1342	50
--(286) 555-6063	(676) 555-6554	43
--(770) 555-1861	(725) 555-3243	49
--(031) 555-6622	(910) 555-3251	38
--(826) 555-1652	(066) 555-9701	55
--(338) 555-6650	(704) 555-2131	54

SELECT passport_number FROM "passengers" WHERE flight_id = 6;
--passport_number
--3835860232
--1618186613
--7179245843
--1682575122
--7597790505
--6128131458
--6264773605
--3642612721

--Final Suspects
--Diana 3592750733
SELECT passport_number FROM "passengers" WHERE flight_id = 6 AND passport_number = 3592750733 ;
--nothing

--Robin accoplece

--Bruce 5773159633
SELECT passport_number FROM "passengers" WHERE flight_id = 6 AND passport_number = 5773159633 ;
--nothing

--name	passport_number
--Philip	3391710505

SELECT destination_airport_id FROM "flights" WHERE id = 36;
--4
SELECT full_name,city FROM "airports" WHERE id = 4;
full_name
LaGuardia Airport
New York City
