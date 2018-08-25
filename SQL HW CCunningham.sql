USE sakila;

#1.A
select first_name, last_name from actor;

#1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`.
#THIS HAS NOT BEEN COMPLETED YET
ALTER TABLE actor
ADD COLUMN Actor_Name Varchar(255);

SET SQL_SAFE_UPDATES=0;

update actor
set Actor_Name = concat(upper(first_name), ' ',upper(last_name)); 

#still need to place in column called "Actor Name"

#2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?

SELECT actor_id FROM actor
WHERE first_name
LIKE "Joe";

#2b. Find all actors whose last name contain the letters `GEN'

SELECT * FROM actor
WHERE last_name
LIKE "%GEN%";

#2c. Find all actors whose last names contain the letters `LI`. This time, order the rows by last name and first name, in that order:

SELECT * FROM actor
WHERE last_name
LIKE "%LI%"
ORDER BY last_name,first_name;

#2d. Using `IN`, display the `country_id` and `country` 
#columns of the following countries: Afghanistan, Bangladesh, and China:

SELECT country id, country FROM country
WHERE country In("China","Afghanistan","Bangladesh");


#3a. You want to keep a description of each actor.

ALTER TABLE actor
ADD COLUMN description BLOB;

#3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the `description` column.

ALTER TABLE actor DROP description;

#4a. List the last names of actors, as well as how many actors have that last name.

SELECT last_name, COUNT(last_name)AS Frequency
FROM actor
  GROUP BY last_name
  ORDER BY
  COUNT(last_name) DESC;

#4b. List last names of actors and the number of actors who have that last name, but only for 
#names that are shared by at least two actors

SELECT last_name, COUNT(last_name)AS Frequency
FROM actor
  GROUP BY last_name
  HAVING COUNT(last_name)>1
  ORDER BY
  COUNT(last_name) DESC;

#4c. The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`. Write a query to fix the record.

SET SQL_SAFE_UPDATES=0;

Update actor 
set first_name="HARPO" 
where first_name="Groucho" AND last_name="Williams";

SET SQL_SAFE_UPDATES=1;

#4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct name after all! 
#In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`.

Update actor 
set first_name="GROUCHO" 
where first_name="Harpo" AND last_name="Williams";

select * from actor where last_name="Williams";

#5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?

#  * Hint: <https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html>

SHOW CREATE TABLE address;

# 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. Use the tables `staff` and `address`:

SELECT first_name, last_name, address FROM staff s
LEFT OUTER JOIN address a
ON (s.address_id = a.address_id);

# 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`.
#THIS HAS NOT BEEN COMPLETED YET - LIKE 4A AS WELL

SELECT first_name, last_name, sum(amount)FROM staff s
LEFT OUTER JOIN payment p
ON (s.staff_id = p.staff_id)
GROUP BY first_name
HAVING payment_date
Like "2005-08%";

select payment_date from payment;

# 6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`.
# Use inner join.

SELECT title, COUNT(actor_id)AS "Total Actors"
FROM film f
INNER JOIN film_actor fa
ON (f.film_id = fa.film_id)
GROUP BY title;

# 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?

select *from inventory;

SELECT COUNT(film_id) FROM inventory
WHERE film_id IN (
   SELECT film_id
	FROM film
	WHERE title='Hunchback Impossible');

# 6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer.
#List the customers alphabetically by last name:

SELECT last_name, sum(amount)AS "Total Paid"
FROM customer c
JOIN payment p
ON (c.customer_id = p.customer_id)
	GROUP BY last_name
	ORDER BY
	last_name ASC;

ORDER BY LAST NAME;

# 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence,
# films starting with the letters `K` and `Q` have also soared in popularity. 
# Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English.
# film has language_id, 

SELECT title FROM film
WHERE title Like "q%" 
OR title Like "k%"
AND language_id IN (
	SELECT language_id 
	FROM language
	WHERE name = "English");

# 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.

SELECT first_name,last_name FROM actor
WHERE actor_id IN (
   SELECT actor_id
	FROM film_actor
	WHERE film_id IN
		(select film_id
        from film where title='Alone Trip'));
        
# 7c. You want to run an email marketing campaign in Canada, for which you will need the names and 
# email addresses of all Canadian customers. Use joins to retrieve this information.

SELECT first_name,last_name,email FROM customer
WHERE address_id IN (
   SELECT address_id
	FROM city
	WHERE country_id IN
		(select country_id
        from country where country='Canada'));

# 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion.
# Identify all movies categorized as family films.

SELECT title FROM film
WHERE film_id IN (
    SELECT film_id
	FROM film_category
	WHERE category_id IN
		(select category_id
        from category where name='Family'));
        
# 7e. Display the most frequently rented movies in descending order.
# show title, sorted by a count by inventory_id (tie back to title, somehow) and sorted by that count in descending order
STILL NOT COMPLETE


SELECT title, count(inventory_id)FROM film
WHERE film_id IN(
	SELECT film_id
    FROM inventory
    WHERE inventory_id IN(
    SELECT 

GROUP BY title
ORDER BY
count(inventory_id);


# 7f. Write a query to display how much business, in dollars, each store brought in.
# return store_id (staff), tie to and return staff_id (staff<->payment), sum(amount) (in payment table)


# 7g. Write a query to display for each store its store ID, city, and country.

select * from store;

# 7h. List the top five genres in gross revenue in descending order. (**Hint**: you may need to use the 
# following tables: category, film_category, inventory, payment, and rental.)



# 8a. In your new role as an executive, you would like to have an easy way of viewing the 
# Top five genres by gross revenue. Use the solution from the problem above to create a view. 
# If you haven't solved 7h, you can substitute another query to create a view.
# Note - as of answering this question, still hadn't solved 7h.

CREATE VIEW 8a AS
SELECT title FROM film
WHERE film_id IN (
    SELECT film_id
	FROM film_category
	WHERE category_id IN
		(select category_id
        from category where name='Family'));

# 8b. How would you display the view that you created in 8a?

select * from 8a;


# 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.

DROP VIEW 8a;

