import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
STAGING = Path("data/staging")
STAGING.mkdir(parents=True, exist_ok=True)

def main():
    # 1. Leer datos crudos
    df = pd.read_csv(RAW / "dim_date.csv")
    print(f"Filas crudas: {len(df)}")

    # 2. Convertir la columna 'date' a tipo fecha
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # 3. Validar que 'year', 'month', 'week', 'quarter' sean numéricos
    for col in ['year','month','week','quarter']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 4. Filtrar valores inválidos
    if 'month' in df.columns:
        df = df[df['month'].between(1,12)]
    if 'quarter' in df.columns:
        df = df[df['quarter'].between(1,4)]
    if 'week' in df.columns:
        df = df[df['week'].between(1,53)]

    # 5. Normalizar nombres de meses
    if 'month_name' in df.columns:
        df['month_name'] = df['month_name'].astype(str).str.strip().str.lower()

    # 6. Eliminar duplicados por date_id
    if 'date_id' in df.columns:
        df = df.drop_duplicates(subset=['date_id'], keep='last')

    # 7. Guardar limpio en staging
    df.to_csv(STAGING / "dim_date.csv", index=False)
    print(f"✅ Guardado limpio: data/staging/dim_date.csv con {len(df)} filas")

if __name__ == "__main__":
    main()