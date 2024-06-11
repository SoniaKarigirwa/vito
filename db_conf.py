import sqlite3
# Connect to SQLite database
try:
    conn = sqlite3.connect('customer_faces_data.db')
    c = conn.cursor()
except sqlite3.Error as e:
    print("SQLite error:", e)

#  ALTER table to store status of the okay_sign detected 
try:
    c.execute('''ALTER TABLE customers ADD COLUMN ok_sign INTEGER DEFAULT 1''')
except sqlite3.Error as e:
    print("SQLite error:", e)