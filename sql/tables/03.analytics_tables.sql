CREATE SCHEMA IF NOT EXISTS analytics;

CREATE TABLE analytics.fact_sales AS
SELECT
    s.transaction_id,
    s.transaction_date,
    d.date_id,
    s.store_id,
    s.customer_id,
    si.product_id,
    si.quantity,
    si.quantity * si.unit_price * (1 - COALESCE(si.discount_pct,0)/100) AS net_revenue,
    si.quantity * si.cost_price AS cost,
    (si.quantity * si.unit_price * (1 - COALESCE(si.discount_pct,0)/100))
      - (si.quantity * si.cost_price) AS margin
FROM staging.sales_transactions s
JOIN staging.sales_items si
  ON s.transaction_id = si.transaction_id
LEFT JOIN staging.dates d
  ON s.transaction_date = d.date;


SELECT
    COUNT(*) AS filas,
    SUM(net_revenue) AS ventas,
    SUM(margin) AS margen
FROM analytics.fact_sales;



CREATE TABLE analytics.dim_products AS
SELECT *
FROM staging.products;

CREATE TABLE analytics.dim_customers AS
SELECT * 
FROM staging.customers;

CREATE TABLE analytics.dim_stores AS
SELECT * 
FROM staging.stores;

CREATE TABLE analytics.dim_dates AS
SELECT * 
FROM staging.dates;

CREATE TABLE analytics.dim_inventory AS
SELECT * 
FROM staging.inventory_snapshot;
