import pandas as pd
import unicodedata
from pathlib import Path

RAW = Path("data/raw")
STAGING = Path("data/staging")
STAGING.mkdir(parents=True, exist_ok=True)

def normalizar_texto(col):
    return col.astype(str).str.strip().str.lower()

def quitar_acentos_mantener_ñ(col):
    col = col.astype(str)
    col = col.apply(lambda x: unicodedata.normalize('NFKD', x))
    col = col.apply(lambda x: ''.join(c for c in x if not unicodedata.combining(c)))
    return col.str.strip().str.lower()

def main():
    # 1. Leer datos crudos
    df = pd.read_csv(RAW / "dim_products.csv")
    print(f"Filas crudas: {len(df)}")

    # 2. Normalizar texto en columnas relevantes
    cols_texto = ['product_name','category','subcategory','brand','season','size','color']
    df[cols_texto] = df[cols_texto].apply(normalizar_texto)

    # 3. Quitar acentos en product_name, category, subcategory, brand, color
    for c in ['product_name','category','subcategory','brand','color']:
        if c in df.columns:
            df[c] = quitar_acentos_mantener_ñ(df[c])

    # 4. Validar precios: cost_price y list_price deben ser positivos
    for col in ['cost_price','list_price']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df = df[df[col] > 0]

    # 5. Validar margen: target_margin_pct entre 0 y 100
    if 'target_margin_pct' in df.columns:
        df['target_margin_pct'] = pd.to_numeric(df['target_margin_pct'], errors='coerce')
        df = df[df['target_margin_pct'].between(0,100)]

    # 6. Eliminar duplicados por product_id
    if 'product_id' in df.columns:
        df = df.drop_duplicates(subset=['product_id'], keep='last')

    # 7. Guardar limpio en staging
    df.to_csv(STAGING / "dim_products.csv", index=False)
    print(f"✅ Guardado limpio: data/staging/dim_products.csv con {len(df)} filas")

if __name__ == "__main__":
    main()

