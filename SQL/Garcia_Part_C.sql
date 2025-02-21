SELECT customer_id,first_name,last_name,address FROM  customer;

SELECT title FROM movie WHERE date >= 30 ORDER BY AGE ASC;

SELECT * FROM distributor ORDER by distributor_name;

UPDATE customer 
SET last_name='Johnson'
WHERE first_name='Samantha';

DELETE FROM customer WHERE first_name='Jamie';