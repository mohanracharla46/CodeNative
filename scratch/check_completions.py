import sqlite3

def check_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    print("--- TASKS ---")
    for row in conn.execute("SELECT * FROM tasks"):
        print(dict(row))
    print("--- USER TASKS COMPLETIONS ---")
    for row in conn.execute("SELECT * FROM user_tasks"):
        print(dict(row))
    conn.close()

if __name__ == '__main__':
    check_db()
