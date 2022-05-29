import sqlite3

from aiogram import Bot
from tgbot.config import load_config
from tgbot.keyboards.notification import notification_keyboard 


async def send_notification(
        bot: Bot,
        ):
    db_connect = sqlite3.connect(load_config().db.path)
    db_cursor = db_connect.cursor()
    db_data = db_cursor.execute(
                """
                select * from tasks 
                where is_active = 0 
                and
                server_date < datetime('now', 'localtime')
                """
                ).fetchall()
    print(db_data)
    for task_data in db_data:
        user_id, task_id, name, description, timezone, user_date, server_date, is_active = [_ for _ in task_data]
        is_active = 1
        db_cursor.execute(
                f"""
                update tasks 
                set is_active = {is_active}
                where task_id = {task_id}
                """)
        text = [  
                "Time!!",
                f"Name: {name}",
                "",
                f"Description: {description}",
                f"Timezone: {timezone}",
                f"Datetime: {user_date}",
                "",
                f"Task ID: {task_id}"
                ]
        await bot.send_message(
                chat_id=user_id,
                text="\n".join(text),
                reply_markup=notification_keyboard)
    db_connect.commit()
    db_connect.close()



