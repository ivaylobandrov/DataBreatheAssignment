#!/bin/bash

echo "Hello, world!"

psql -U $POSTGRES_USER -d $POSTGRES_DB -c "CREATE TABLE customer(customer_id int PRIMARY KEY, home_store int, customer_first_name text, customer_email text, customer_since DATE, loyalty_card_number TEXT, birthdate DATE, gender text, birth_year int)"
psql -U $POSTGRES_USER -d $POSTGRES_DB -c "CREATE TABLE product(product_id int PRIMARY KEY, product_group text, product_category text, product_type text, product text, product_description text, unit_of_measure text, current_wholesale_price decimal, current_retail_price text, tax_exampt_yn text, promo_yn text, new_product_yn text)"
psql -U $POSTGRES_USER -d $POSTGRES_DB -c "CREATE TABLE sales(transaction_id int PRIMARY KEY, transaction_date date, transaction_time time, sales_outlet_id int, staff_id int, customer_id int, instore_yn text, order_number int, line_item_id int, product_id int, quantity int, line_item_amount decimal, unit_price decimal, promo_item_yn text)"

psql -U $POSTGRES_USER -d $POSTGRES_DB -c "\copy customer from /csv/customer.csv delimiter ',' CSV HEADER"
psql -U $POSTGRES_USER -d $POSTGRES_DB -c "\copy product from /csv/product.csv delimiter ',' CSV HEADER"
