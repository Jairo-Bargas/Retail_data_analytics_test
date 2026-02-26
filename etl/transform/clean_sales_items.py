import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
STAGING = Path("data/staging")
STAGING.mkdir(parents=True, exist_ok=True)

def main():
    # 1. Leer datos crudos
    df = pd.read_csv(RAW / "sales_items.csv")
    print(f"Filas crudas: {len(df)}")

    # 2. Validar quantity (>=1)
    if 'quantity' in df.columns:
        df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
        df = df[df['quantity'] >= 1]

    # 3. Validar unit_price (>0)
    if 'unit_price' in df.columns:
        df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
        df = df[df['unit_price'] > 0]

    # 4. Validar discount_pct (0–100)
    if 'discount_pct' in df.columns:
        df['discount_pct'] = pd.to_numeric(df['discount_pct'], errors='coerce')
        df = df[df['discount_pct'].between(0,100)]

    # 5. Validar cost_price (>0)
    if 'cost_price' in df.columns:
        df['cost_price'] = pd.to_numeric(df['cost_price'], errors='coerce')
        df = df[df['cost_price'] > 0]

    # 6. Eliminar duplicados por combinación transaction_id + product_id
    if {'transaction_id','product_id'}.issubset(df.columns):
        df = df.drop_duplicates(subset=['transaction_id','product_id'], keep='last')

    # 7. Guardar limpio en staging
    df.to_csv(STAGING / "sales_items.csv", index=False)
    print(f"✅ Guardado limpio: data/staging/sales_items.csv con {len(df)} filas")

if __name__ == "__main__":
    main()