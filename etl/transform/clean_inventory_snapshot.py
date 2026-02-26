import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
STAGING = Path("data/staging")
STAGING.mkdir(parents=True, exist_ok=True)

def main():
    # 1. Leer datos crudos
    df = pd.read_csv(RAW / "inventory_snapshot.csv")
    print(f"Filas crudas: {len(df)}")

    # 2. Convertir snapshot_date a tipo fecha
    if 'snapshot_date' in df.columns:
        df['snapshot_date'] = pd.to_datetime(df['snapshot_date'], errors='coerce')

    # 3. Validar stock_qty (>=0)
    if 'stock_qty' in df.columns:
        df['stock_qty'] = pd.to_numeric(df['stock_qty'], errors='coerce')
        df = df[df['stock_qty'] >= 0]

    # 4. Eliminar duplicados por combinación snapshot_date + product_id + store_id
    if {'snapshot_date','product_id','store_id'}.issubset(df.columns):
        df = df.drop_duplicates(subset=['snapshot_date','product_id','store_id'], keep='last')

    # 5. Guardar limpio en staging
    df.to_csv(STAGING / "inventory_snapshot.csv", index=False)
    print(f"✅ Guardado limpio: data/staging/inventory_snapshot.csv con {len(df)} filas")

if __name__ == "__main__":
    main()