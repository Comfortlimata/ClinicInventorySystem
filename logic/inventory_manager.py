from ui.database_setup import get_db_connection
from datetime import datetime

def add_medicine(name, category, quantity, unit, expiry_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO medicines (name, category, quantity, unit, expiry_date, date_added) VALUES (?, ?, ?, ?, ?, ?)",
        (name, category, quantity, unit, expiry_date, datetime.now().strftime("%Y-%m-%d"))
    )
    conn.commit()
    conn.close()

def get_all_medicines():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicines")
    results = cursor.fetchall()
    conn.close()
    return results
