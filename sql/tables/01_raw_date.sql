
-- Tabla: raw.date
-- Fuente: dim_date.csv
-- Descripción: Datos crudos de fechas tal como vienen del origen


CREATE TABLE IF NOT EXISTS raw.dates (
    date_id INTEGER,
    date DATE,
    year INTEGER,
    month INTEGER,
    month_name TEXT,
    week INTEGER,
    quarter INTEGER
);
