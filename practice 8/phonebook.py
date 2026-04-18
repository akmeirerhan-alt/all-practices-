# phonebook.py
from connect import connect

def main():
    conn = connect()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()

        # --- Task 1: Pattern Search ---
        print("\n--- Task 1: Testing Pattern Search ---")
        cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", ('Akmeir',))
        for row in cur.fetchall():
            print(row)

        # --- Task 2: Upsert ---
        print("\n--- Task 2: Testing Upsert (Insert or Update) ---")
        cur.execute("CALL upsert_contact(%s, %s, %s)", ('Alikhan', 'S', '87001234567'))
        conn.commit()
        print("Upsert successful.")

        # --- Task 3: Bulk Insert with Validation ---
        print("\n--- Task 3: Testing Bulk Insert ---")
        names = ['User1', 'User2', 'InvalidUser']
        phones = ['77711122233', '77755566677', '123'] # '123' is too short
        cur.execute("CALL insert_many_contacts(%s, %s, NULL)", (names, phones))
        invalid = cur.fetchone()
        print(f"Invalid records returned from DB: {invalid}")
        conn.commit()

        # --- Task 4: Pagination ---
        print("\n--- Task 4: Testing Pagination (Limit 2, Offset 0) ---")
        cur.execute("SELECT * FROM get_contacts_paged(%s, %s)", (2, 0))
        for row in cur.fetchall():
            print(row)

        # --- Task 5: Delete ---
        print("\n--- Task 5: Testing Delete ---")
        cur.execute("CALL delete_contact(%s)", ('User1',))
        conn.commit()
        print("Delete successful.")

        cur.close()
    except Exception as e:
        print(f"Error during execution: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()