import psycopg2

conn = psycopg2.connect(
    host="localhost",      # o la IP de tu contenedor
    port=5435,             # asegúrate del puerto correcto
    database="retail_db",
    user="app_user",
    password="app_password"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM raw.customers LIMIT 5;")
print(cursor.fetchall())

conn.close()
