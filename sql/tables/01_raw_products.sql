-- Tabla: raw.products
-- Fuente: dim_products.csv
-- Descripción: Datos crudos de productos tal como vienen del origen

CREATE TABLE IF NOT EXISTS raw.products (
    product_id INTEGER,
    product_name VARCHAR(150),
    category VARCHAR(50),
    subcategory VARCHAR(50),
    brand VARCHAR(50),
    season VARCHAR(30),
    size VARCHAR(20),
    color VARCHAR(30),
    cost_price NUMERIC(10,2),
    list_price NUMERIC(10,2),
    target_margin_pct NUMERIC(5,2),
    PRIMARY KEY (product_id)
);
