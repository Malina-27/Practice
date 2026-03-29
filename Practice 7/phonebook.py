from connect import connect

def insert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added!")




from connect import connect

def search_by_name(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s",
        (f"%{name}%",)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()



def update_phone(name, new_phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s",
        (new_phone, name)
    )

    conn.commit()

    cur.close()
    conn.close()

    print("Updated!")



def delete_contact(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE name = %s",
        (name,)
    )

    conn.commit()

    cur.close()
    conn.close()

    print("Deleted!")

import csv
from connect import connect

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()

    print("CSV imported successfully!")

def search_by_phone_prefix(prefix):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
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

menu()