-- Tabla: raw.stores
-- Fuente: dim_stores.csv
-- Descripción: Datos crudos de tiendas tal como vienen del origen

CREATE TABLE IF NOT EXISTS raw.stores (
    store_id INTEGER PRIMARY KEY,
    store_name VARCHAR(100),
    city VARCHAR(50),
    country VARCHAR(50),
    channel VARCHAR(50)
)