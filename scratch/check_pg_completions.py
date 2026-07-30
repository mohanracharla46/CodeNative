import sys
import os
sys.path.append(os.path.abspath('.'))
from app import get_db_connection, execute_query, release_db_connection

def check_db():
    conn = get_db_connection()
    print("--- TASKS ---")
    for row in execute_query(conn, "SELECT id, title, points, created_at FROM tasks").fetchall():
        print(dict(row))
    print("--- USER TASKS COMPLETIONS ---")
    for row in execute_query(conn, "SELECT * FROM user_tasks").fetchall():
        print(dict(row))
    release_db_connection(conn)

if __name__ == '__main__':
    check_db()
