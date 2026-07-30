import sqlite3

def list_users():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.execute("SELECT id, name, email, is_admin FROM users")
    users = cursor.fetchall()
    for u in users:
        print(f"ID: {u['id']}, Name: {u['name']}, Email: {u['email']}, Admin: {u['is_admin']}")
    conn.close()

if __name__ == '__main__':
    list_users()
