-- Tabla: raw.sales_transactions
-- Fuente: sales_transactions.csv
-- Descripción: Datos crudos de transacciones tal como vienen del origen


CREATE TABLE IF NOT EXISTS raw.sales_transactions (
    transaction_id INTEGER,
    transaction_date DATE,
    store_id INTEGER,
    customer_id INTEGER,
    channel VARCHAR(50),
    payment_method VARCHAR(50)
);