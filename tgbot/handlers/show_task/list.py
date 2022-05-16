import sqlite3

from aiogram import types, Bot, Dispatcher

from tgbot.config import load_config


async def show_list(cb: types.CallbackQuery):
    token = load_config().tg_bot.token
    user_id = cb.message.from_user.id
    
    db_list = sqlite3.connect("db/main.db")
    db_list = list(db_list.cursor().execute("select * from tasks").fetchall()) 
    

    for l in db_list:
       if l[0] != user_id:
           db_list.remove(l)
    
    text = "Choose your task:"

    await Bot(token=token).edit_message_text(
            chat_id=cb.message.chat.id,
            message_id=cb.message.message_id,
            text=text)


def register_show_list(dp: Dispatcher):
    dp.register_callback_query_handler(
            show_list,
            text="my_tasks")
