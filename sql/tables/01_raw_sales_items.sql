-- Tabla: raw.sales_items
-- Fuente: sales_items.csv
-- Descripción: Datos crudos de ventas tal como vienen del origen

CREATE TABLE IF NOT EXISTS raw.sales_items (
    transaction_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price NUMERIC(10,2),
    discount_pct NUMERIC(5,2),
    cost_price NUMERIC(10,2)
);

