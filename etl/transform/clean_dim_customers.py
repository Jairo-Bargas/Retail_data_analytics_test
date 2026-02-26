import pandas as pd
import unicodedata
from pathlib import Path

RAW = Path("data/raw")
STAGING = Path("data/staging")
STAGING.mkdir(parents=True, exist_ok=True)

def normalizar_texto(col):
    # Convierte todo a string, quita espacios y pasa a minúsculas
    return col.astype(str).str.strip().str.lower()

def quitar_acentos_mantener_ñ(col):
    # Quita acentos pero mantiene la ñ
    col = col.astype(str)
    col = col.apply(lambda x: unicodedata.normalize('NFKD', x))
    col = col.apply(lambda x: ''.join(c for c in x if not unicodedata.combining(c)))
    return col.str.strip().str.lower()

def main():
    # 1. Leer datos crudos
    df = pd.read_csv(RAW / "dim_customers.csv")
    print(f"Filas crudas: {len(df)}")

    # 2. Normalizar texto en columnas relevantes
    cols_texto = [c for c in ['customer_name','segment','city','country'] if c in df.columns]
    df[cols_texto] = df[cols_texto].apply(normalizar_texto)

    # 3. Quitar acentos en nombre, ciudad y país
    for c in ['customer_name','city','country']:
        if c in df.columns:
            df[c] = quitar_acentos_mantener_ñ(df[c])

    # 4. Validar edades (0–100)
    if 'age' in df.columns:
        df = df[df['age'].between(0,100)]

    # 5. Eliminar duplicados por customer_id
    if 'customer_id' in df.columns:
        df = df.drop_duplicates(subset=['customer_id'], keep='last')

    # 6. Convertir customer_id a string (si lo querés como clave textual)
    df['customer_id'] = df['customer_id'].astype(str)

    # 7. Guardar limpio en staging
    df.to_csv(STAGING / "dim_customers.csv", index=False)
    print(f"✅ Guardado limpio: data/staging/dim_customers.csv con {len(df)} filas")

if __name__ == "__main__":
    main()