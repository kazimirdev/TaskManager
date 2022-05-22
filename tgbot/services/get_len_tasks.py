import sqlite3


def get_len_task(user_id: int):
    db_conn = sqlite3.connect("db/main.db")
    return  db_conn.cursor().execute(
        'select count(*) from tasks where user_id=:id',
        {"id": user_id}).fetchone()[0]
    
