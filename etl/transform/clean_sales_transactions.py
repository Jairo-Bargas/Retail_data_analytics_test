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
    df = pd.read_csv(RAW / "sales_transactions.csv")
    print(f"Filas crudas: {len(df)}")

    # 2. Convertir transaction_date a tipo fecha
    if 'transaction_date' in df.columns:
        df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')

    # 3. Normalizar texto en channel y payment_method
    for c in ['channel','payment_method']:
        if c in df.columns:
            df[c] = quitar_acentos_mantener_ñ(df[c])

    # 4. Validar channel (solo 'physical' o 'online')
    if 'channel' in df.columns:
        df['channel_valido'] = df['channel'].isin(['physical','online'])

    # 5. Eliminar duplicados por transaction_id
    if 'transaction_id' in df.columns:
        df = df.drop_duplicates(subset=['transaction_id'], keep='last')

    # 6. Guardar limpio en staging
    df.to_csv(STAGING / "sales_transactions.csv", index=False)
    print(f"✅ Guardado limpio: data/staging/sales_transactions.csv con {len(df)} filas")

if __name__ == "__main__":
    main()