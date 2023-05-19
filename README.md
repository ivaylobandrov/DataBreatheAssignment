# DataBreathe Assignment

Basic FastApi to get customer's data related to sales. Python 3.10 used.

# Steps to run the FastApi app:

1. We assume that you have already installed python 3.10 and Docker on your system. If you haven't done so, you can download it from the official sites:
   - https://www.python.org/downloads/
   - https://www.docker.com/products/docker-desktop/

2. Build the project and the database containers in the terminal using the following command (Should be located in the project's main directory):
   - docker build -t python-app:latest .

# Steps to create the database and the corresponding tables:

Please note that the database is not available, it was used only for testing purposes. In order to
use it a postgres database should be created and the data from the provided csv files have to be ingested in the corresponding tables.
An example of how you can create the necessary database and tables:

1. To create the database you can use the following command:
   - psql -U postgres -c "CREATE DATABASE postgres;"
2. Connect to the postgres database with:
   - psql postgres://postgres:postgres@localhost:5432/postgres
3. Example of how a table with the corresponding columns can be created:
   - CREATE TABLE customer(customer_id int PRIMARY KEY, home_store int, customer_first_name text, customer_email text, customer_since DATE, loyalty_card_number TEXT, birthdate DATE, gender text, birth_year int);
4. Ingest data from a csv file in to the new table:
   - \copy customer from /Users/ivaylobandrov/Desktop/csvdata/dataset/customer.csv delimiter ',' CSV HEADER

# Steps to run the tests:

1. Execute the following command:
   - python -m pytest