INSERT INTO producer (producer_id, companyname, country)
VALUES('1', 'movie place', 'USA');
INSERT INTO producer (producer_id, companyname, country)
VALUES('2', 'movie zone', 'China');
INSERT INTO producer (producer_id, companyname, country)
VALUES('3', 'movie spot', 'UK');
INSERT INTO producer (producer_id, companyname, country)
VALUES('4', 'movie store', 'Japan');
INSERT INTO producer (producer_id, companyname, country)
VALUES('5', 'movie hub', 'Canada');

INSERT INTO movie (movie_id, title, duration, rating, awardwon, releasedate)
VALUES('22', 'the guyver', '2H 12M', '7', 'emmy', 1989-01-01);
INSERT INTO movie (movie_id, title, duration, rating, awardwon, releasedate)
VALUES('20', 'Titanic', '3H 30M', '2', 'oscar', 1995-04-03);
INSERT INTO movie (movie_id, title, duration, rating, awardwon, releasedate)
VALUES('2', 'MallRats', '2H', '8', 'none', 2007-05-05);
INSERT INTO movie (movie_id, title, duration, rating, awardwon, releasedate)
VALUES('33', 'Lord of the rings', '3H 50M', '10', 'golden globe', 1989-09-09);
INSERT INTO movie (movie_id, title, duration, rating, awardwon, releasedate)
VALUES('50', 'upside down', '2H 1M', '4', 'kids choice', 2020-10-11);

INSERT INTO customer_movie (date_rented, date_returned, damage, rentalID, late, due_date)
VALUES('11-19-24', '11-22-24', 'no', '111', 'no', '11-22-24');
INSERT INTO customer_movie (date_rented, date_returned, damage, rentalID, late, due_date)
VALUES('01-02-24', '01-02-24', 'no', '11', 'no', '01-02-24');
INSERT INTO customer_movie (date_rented, date_returned, damage, rentalID, late, due_date)
VALUES('10-18-24', '10-22-24', 'no', '1', 'yes', '10-20-24');
INSERT INTO customer_movie (date_rented, date_returned, damage, rentalID, late, due_date)
VALUES('12-01-24', '12-01-24', 'no', '2', 'no', '12-01-24');
INSERT INTO customer_movie (date_rented, date_returned, damage, rentalID, late, due_date)
VALUES('11-10-24', '11-15-24', 'yes', '22', 'no', '11-15-24');

INSERT INTO customer (customer_id, first_name, last_name, address, phone_number, birthdate)
VALUES('1', 'Jamie', 'Garcia', '11 2nd street', '1231234567', '4-22-22');
INSERT INTO customer (customer_id, first_name, last_name, address, phone_number, birthdate)
VALUES('2', 'Jim', 'Thompson', '22 1st street', '9092232232', '4-21-98');
INSERT INTO customer (customer_id, first_name, last_name, address, phone_number, birthdate)
VALUES('3', 'Samantha', 'White', '101 8th street', '7146152907', '5-12-09');
INSERT INTO customer (customer_id, first_name, last_name, address, phone_number, birthdate)
VALUES('4', 'Paul', 'liston', '989 7th street', '9511230000', '2-01-01');
INSERT INTO customer (customer_id, first_name, last_name, address, phone_number, birthdate)
VALUES('5', 'Ted', 'Smith', '245 2nd Ave.', '8005670200', '2-14-00');

INSERT INTO distributor (distributor_id, distributor_name, price, stock)
VALUES('55', 'Costco', 3.75, '14');
INSERT INTO distributor (distributor_id, distributor_name, price, stock)
VALUES('5', 'Target', 3.60, '13');
INSERT INTO distributor (distributor_id, distributor_name, price, stock)
VALUES('555', 'Amazon', 4.00, '12');
INSERT INTO distributor (distributor_id, distributor_name, price, stock)
VALUES('12', 'My Distributor', 3.25, '11');
INSERT INTO distributor (distributor_id, distributor_name, price, stock)
VALUES('1', 'Sams Club', 4.50, '10');

INSERT INTO format (format_id, format_type)
VALUES('1', 'VHS');
INSERT INTO format (format_id, format_type)
VALUES('2', 'Digital');
INSERT INTO format (format_id, format_type)
VALUES('3', 'HDDVD');
INSERT INTO format (format_id, format_type)
VALUES('4', 'Blueray');
INSERT INTO format (format_id, format_type)
VALUES('5', 'DVD');

INSERT INTO actor (actor_id, actor_firstname, actor_lastname)
VALUES('567', 'Brad', 'Pitt');
INSERT INTO actor (actor_id, actor_firstname, actor_lastname)
VALUES('7', 'Micheal', 'cera');
INSERT INTO actor (actor_id, actor_firstname, actor_lastname)
VALUES('5', 'Elijah', 'Wood');
INSERT INTO actor (actor_id, actor_firstname, actor_lastname)
VALUES('6', 'Keanue', 'Reaves');
INSERT INTO actor (actor_id, actor_firstname, actor_lastname)
VALUES('11', 'Seth', 'Rogan');


INSERT INTO award (award_id, award_name)
VALUES('4444', 'Emmy');
INSERT INTO award (award_id, award_name)
VALUES('17', 'Tony');
INSERT INTO award (award_id, award_name)
VALUES('12', 'Academy award');
INSERT INTO award (award_id, award_name)
VALUES('2', 'Oscar');
INSERT INTO award (award_id, award_name)
VALUES('36', 'Golden Globe');


