from connect import connect

conn = connect()
cur = conn.cursor()

# добавить контакт
cur.execute("CALL upsert_contact(%s, %s)", ("Ali", "87001234567"))

# поиск
cur.execute("SELECT * FROM search_contacts(%s)", ("Ali",))
rows = cur.fetchall()

print("Search result:")
for row in rows:
    print(row)

# пагинация
cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (5, 0))
rows = cur.fetchall()

print("Paginated:")
for row in rows:
    print(row)

conn.commit()
cur.close()
conn.close()