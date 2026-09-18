import mysql.connector
import os

SQL_FILE = os.path.join(os.path.dirname(__file__), 'migrations', '003_hr_egypt_rates_mysql.sql')

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Hazem@2026',
    'database': 'customs_portal'
}

if not os.path.exists(SQL_FILE):
    print('Migration file not found:', SQL_FILE)
    raise SystemExit(1)

with open(SQL_FILE, 'r', encoding='utf-8') as f:
    sql = f.read()

# Split statements; naive split on ';' but keep delimiters inside JSON safe by simple approach: execute whole file with cursor.execute() if connector supports multi.
try:
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor()
    # execute as multi
    for result in cur.execute(sql, multi=True):
        if result.with_rows:
            print('Result:', result.fetchall())
        else:
            print('Executed statement, affected rows:', result.rowcount)
    conn.commit()
    cur.close()
    conn.close()
    print('Migration applied successfully.')
except mysql.connector.Error as e:
    print('MySQL error:', e)
    raise
except Exception as e:
    print('Error:', e)
    raise
