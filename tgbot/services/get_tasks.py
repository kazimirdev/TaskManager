import sqlite3

from tgbot.config import load_config


def get_task(user_id: int, page: int = 1):
    db_conn = sqlite3.connect(load_config().db.path)
    db_list = db_conn.cursor().execute(
        'select * from tasks where user_id=:id',
        {"id": user_id}).fetchall()
    return db_list[page - 1] 
    
