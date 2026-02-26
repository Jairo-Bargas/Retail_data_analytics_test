-- Tabla: raw.inventory_snapshot
-- Fuente: inventory_snapshot.csv
-- Descripción: Datos crudos de inventario tal como vienen del origen

CREATE TABLE IF NOT EXISTS raw.inventory_snapshot (
    snapshot_date DATE,
    product_id INTEGER,
    store_id INTEGER,
    stock_qty INTEGER
);
