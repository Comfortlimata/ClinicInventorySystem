from ui.database_setup import get_db_connection
from datetime import datetime, timedelta

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

def get_expiring_medicines(days=30):
    conn = get_db_connection()
    cursor = conn.cursor()
    today = datetime.now().date()
    future = today + timedelta(days=days)
    cursor.execute("SELECT * FROM medicines WHERE expiry_date IS NOT NULL AND expiry_date != '' AND DATE(expiry_date) <= ?", (future.strftime("%Y-%m-%d"),))
    results = cursor.fetchall()
    conn.close()
    return results
