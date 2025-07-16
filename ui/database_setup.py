import sqlite3

def get_db_connection():
    return sqlite3.connect("rural_inventory.db")

def init_db():
    conn = sqlite3.connect("rural_inventory.db")
    cursor = conn.cursor()

    # Create medicines table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        quantity INTEGER NOT NULL,
        unit TEXT,
        expiry_date TEXT,
        date_added TEXT
    )
    """)

    # Create stock log table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medicine_id INTEGER,
        change_type TEXT,
        quantity INTEGER,
        notes TEXT,
        date_time TEXT,
        FOREIGN KEY (medicine_id) REFERENCES medicines(id)
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Database and tables created successfully.") 