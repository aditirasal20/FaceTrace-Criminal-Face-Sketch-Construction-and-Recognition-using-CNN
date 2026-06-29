"""
Run this ONCE to migrate your existing image_details.db records into Firestore.
    python migrate_to_firestore.py

After running, verify the data in the Firebase console, then you can delete image_details.db.
"""

import sqlite3
from firestore_db import add_face

def migrate():
    conn = sqlite3.connect('image_details.db')
    cursor = conn.cursor()

    # Try with crime column first, fall back if it doesn't exist yet
    try:
        cursor.execute("SELECT filename, name, age, dob, crime FROM image_details")
        rows = cursor.fetchall()
        conn.close()

        print(f'[Migrate] Found {len(rows)} records in SQLite. Uploading to Firestore...\n')
        for row in rows:
            filename, name, age, dob, crime = row
            add_face(filename, name, age, dob, crime)

    except sqlite3.OperationalError:
        # crime column doesn't exist — migrate without it
        cursor.execute("SELECT filename, name, age, dob FROM image_details")
        rows = cursor.fetchall()
        conn.close()

        print(f'[Migrate] Found {len(rows)} records (no crime column). Uploading...\n')
        for row in rows:
            filename, name, age, dob = row
            add_face(filename, name, age, dob, crime='Not on record')

    print('\n[Migrate] Done. Check your Firestore console to verify.')

if __name__ == '__main__':
    migrate()