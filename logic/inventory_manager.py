from ui.database_setup import get_db_connection

def add_medicine(name, quantity, expiry_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO medicines (name, quantity, expiry_date) VALUES (?, ?, ?)",
                   (name, quantity, expiry_date))
    conn.commit()
    conn.close()

def get_all_medicines():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicines")
    results = cursor.fetchall()
    conn.close()
    return results
