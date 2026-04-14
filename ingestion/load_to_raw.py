import psycopg2
from psycopg2.extras import execute_values
from db import get_connection

def load_to_raw(df, table_name):
    conn = get_connection()
    cursor = conn.cursor()

    # Create table dynamically
    columns = ", ".join(df.columns)

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS raw.{table_name} (
            {', '.join([col + ' TEXT' for col in df.columns])}
        );
    """)

    # Insert data
    values = [tuple(x) for x in df.to_numpy()]

    execute_values(
        cursor,
        f"INSERT INTO raw.{table_name} ({columns}) VALUES %s",
        values
    )

    conn.commit()
    cursor.close()
    conn.close()

    print(f"{table_name} loaded")


