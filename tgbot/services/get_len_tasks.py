import sqlite3

from tgbot.config import load_config


def get_len_task(user_id: int):
    db_conn = sqlite3.connect(load_config().db.path)
    return  db_conn.cursor().execute(
        'select count(*) from tasks where user_id=:id',
        {"id": user_id}).fetchone()[0]
    
