import sqlite3

from aiogram import types, Bot, Dispatcher

from tgbot.config import load_config
from tgbot.keyboards.main_menu import main_menu_keyboard


async def del_task(cb: types.CallbackQuery):
    prefix = cb.message.text.split("\n")[0]
    t_id = int(cb.message.text.split(" ")[-1])
    token = load_config().tg_bot.token
    db = sqlite3.connect(load_config().db.path)
    print("------------")
    print("t_id: ", t_id)
    print("------------")
    db.cursor().execute(
            "delete from tasks where task_id=:t_id",
            {"t_id": t_id})
    db.commit()
    if prefix == "Time!!":
        await cb.message.delete()
    else:
        await Bot(token=token).edit_message_text(
                chat_id=cb.message.chat.id,
                message_id=cb.message.message_id,
                text="\n".join([
                    "Task has been deleted.", 
                    "",
                    "Choose what you need"]),
                reply_markup=main_menu_keyboard)


def register_del_task(dp: Dispatcher):
    dp.register_callback_query_handler(
            del_task,
            text="del_task")
