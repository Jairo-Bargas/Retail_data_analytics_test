CREATE TABLE staging.customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    segment TEXT,
    age INTEGER,
    city TEXT,
    country TEXT
);

CREATE TABLE staging.dates (
    date_id INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    month_name TEXT,
    week INTEGER,
    quarter INTEGER
);

CREATE TABLE staging.products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    subcategory TEXT,
    brand TEXT,
    season TEXT,
    size TEXT,
    color TEXT,
    cost_price NUMERIC(10,2),
    list_price NUMERIC(10,2),
    target_margin_pct NUMERIC(5,2)
);

CREATE TABLE staging.stores (
    store_id INTEGER PRIMARY KEY,
    store_name TEXT,
    city TEXT,
    country TEXT,
    channel TEXT
);

CREATE TABLE staging.inventory_snapshot (
	snapshot_date DATE NOT NULL,
	product_id INTEGER NOT NULL,
	store_id INTEGER NOT NULL,
	stock_qty INTEGER NOT NULL
);

CREATE TABLE staging.sales_items (
	transaction_id INTEGER	NOT NULL,
	product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL,
    discount_pct NUMERIC(5,2),
    cost_price NUMERIC(10,2)
);

CREATE TABLE staging.sales_transactions (
    transaction_id INTEGER PRIMARY KEY,
    transaction_date DATE NOT NULL,
    store_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    channel TEXT,
    payment_method TEXT,
    channel_valido BOOLEAN
);

SELECT * FROM staging.customers;
SELECT * FROM staging.dates;
SELECT * FROM staging.inventory_snapshot;
SELECT * FROM staging.products;
SELECT * FROM staging.sales_items;
SELECT * FROM staging.sales_transactions;
SELECT * FROM staging.stores;

