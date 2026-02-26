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
    df = pd.read_csv(RAW / "dim_stores.csv")
    print(f"Filas crudas: {len(df)}")

    # 2. Normalizar texto en columnas relevantes
    cols_texto = ['store_name','city','country','channel']
    df[cols_texto] = df[cols_texto].apply(normalizar_texto)

    # 3. Quitar acentos en store_name, city, country
    for c in ['store_name','city','country']:
        if c in df.columns:
            df[c] = quitar_acentos_mantener_ñ(df[c])

    # 4. Validar que channel sea uno de los valores esperados
    if 'channel' in df.columns:
        df = df[df['channel'].isin(['physical','online'])]

    # 5. Eliminar duplicados por store_id
    if 'store_id' in df.columns:
        df = df.drop_duplicates(subset=['store_id'], keep='last')

    # 6. Guardar limpio en staging
    df.to_csv(STAGING / "dim_stores.csv", index=False)
    print(f"✅ Guardado limpio: data/staging/dim_stores.csv con {len(df)} filas")

if __name__ == "__main__":
    main()