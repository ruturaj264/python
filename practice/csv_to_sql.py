import pandas as pd
import os

# Change this to the folder where your CSVs are located
csv_dir = "C:\\Users\\rrutu\\Desktop\\DataBricks\\ECOM_DB"
output_sql_file = os.path.join(csv_dir, "ecommerce_full_data_inserts.sql")

# List of tables and their column order (to ensure correct order)
tables = [
    "customers",
    "products",
    "orders",
    "order_items",
    "payments",
    "product_reviews"
]

def escape_sql(value):
    if pd.isna(value):
        return 'NULL'
    elif isinstance(value, str):
        return "'" + value.replace("'", "''") + "'"
    elif isinstance(value, bool):
        return 'TRUE' if value else 'FALSE'
    else:
        return f"'{value}'" if isinstance(value, (pd.Timestamp, pd.Timestamp)) else str(value)

with open(output_sql_file, "w", encoding="utf-8") as f:
    for table in tables:
        csv_path = os.path.join(csv_dir, f"{table}.csv")
        df = pd.read_csv(csv_path)
        cols = ', '.join(df.columns)
        f.write(f"-- INSERTS FOR TABLE: {table}\n")
        for _, row in df.iterrows():
            values = ', '.join(escape_sql(row[col]) for col in df.columns)
            insert_stmt = f"INSERT INTO {table} ({cols}) VALUES ({values});"
            f.write(insert_stmt + "\n")
        f.write("\n")

print(f"✅ All INSERT statements saved to: {output_sql_file}")