import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)


def load_csv_to_table(csv_path, table_name, schema="raw"):
    df = pd.read_csv(csv_path)

    df.to_sql(
        name=table_name,
        con=engine,
        schema=schema,
        if_exists="append",
        index=False
    )

    print(f"✔ Datos cargados en {schema}.{table_name}")


BASE_PATH = "data/raw"


if __name__ == "__main__":
   load_csv_to_table(
        f"{BASE_PATH}/dim_products.csv",
        "products"
    )
   load_csv_to_table(
        f"{BASE_PATH}/dim_stores.csv",
        "stores"
    )
   load_csv_to_table(
        f"{BASE_PATH}/inventory_snapshot.csv",
        "inventory_snapshot"
    )
   load_csv_to_table(
        f"{BASE_PATH}/sales_items.csv",
        "sales_items"
    )
   load_csv_to_table(
        f"{BASE_PATH}/sales_transactions.csv",
        "sales_transactions"
    )

   """ load_csv_to_table(
        f"{BASE_PATH}/dim_customers.csv",
        "customers"
    ) """


""" load_csv_to_table(
        f"{BASE_PATH}/dim_date.csv",
        "dates"
    ) """

    




