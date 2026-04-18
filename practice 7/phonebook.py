import csv

from connect import get_connection

def insert_contact(name, phone):
    
    conn = get_connection()
    if not conn: return
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added!")

def search_by_name(name):
    conn = get_connection()
    if not conn: return
    cur = conn.cursor()

    # 使用 ILIKE 进行模糊查询
    cur.execute(
        "SELECT * FROM phonebook WHERE first_name ILIKE %s",
        (f"%{name}%",)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

def update_phone(name, new_phone):
    conn = get_connection()
    if not conn: return
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET phone_number = %s WHERE first_name = %s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Updated!")

def delete_contact(name):
    conn = get_connection()
    if not conn: return
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE first_name = %s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Deleted!")

def insert_from_csv(filename):
    conn = get_connection()
    if not conn: return
    cur = conn.cursor()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            # 跳过第一行表头
            next(file) 
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 3:
                    # CSV 格式: first_name, last_name, phone_number
                    cur.execute(
                        "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                        (row[0], row[1], row[2])
                    )
        conn.commit()
        print("CSV imported successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

def search_by_phone_prefix(prefix):
    conn = get_connection()
    if not conn: return
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE phone_number LIKE %s",
        (prefix + "%",)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

def menu():
    while True:
        print("""
        ===== PHONEBOOK MENU =====
        1. Add contact
        2. Search contact by name
        3. Update contact
        4. Delete contact
        5. Search by phone prefix
        6. Import from CSV
        7. Exit
        """)

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_contact(name, phone)

        elif choice == "2":
            name = input("Search name: ")
            search_by_name(name)

        elif choice == "3":
            name = input("Name to update: ")
            phone = input("New phone: ")
            update_phone(name, phone)

        elif choice == "4":
            name = input("Name to delete: ")
            delete_contact(name)

        elif choice == "5":
            prefix = input("Enter phone prefix (e.g. 8700): ")
            search_by_phone_prefix(prefix)

        elif choice == "6":
            insert_from_csv("contacts.csv")

        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    menu()