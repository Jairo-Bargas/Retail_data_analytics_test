
-- Tabla: raw.customers
-- Fuente: dim_customers.csv
-- Descripción: Datos crudos de clientes tal como vienen del origen

CREATE TABLE IF NOT EXISTS raw.customers (
    customer_id INTEGER,
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    age INTEGER,
    city VARCHAR(100),
    country VARCHAR(50)
);
