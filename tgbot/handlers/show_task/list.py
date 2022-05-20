import sqlite3

from aiogram import types, Bot, Dispatcher

from tgbot.config import load_config
from tgbot.keyboards.pagination import pagination_cb, task_pagination
from tgbot.services.get_tasks import get_task

async def show_first_task(cb: types.CallbackQuery):
    token = load_config().tg_bot.token
    user_id = cb.from_user.id

    db_list = get_task(user_id=user_id)
    print(user_id)
    print(db_list)

    if len(db_list) == 0:
        await cb.answer(
                show_alert=True,
                text="You don't have any tasks!")
    else:
        # dt - data from taks
        dt = db_list[0]
        text = [
                f"Name: {dt[2]}",
                f"Description: {dt[3]}",
                f"Timezone: {dt[4]}",
                f"Datetime: {dt[5]}",
                "",
                f"Task ID: {dt[1]}"
                ]
        await Bot(token=token).edit_message_text(
            chat_id=cb.message.chat.id,
            message_id=cb.message.message_id,
            text="\n".join(text),
            reply_markup=task_pagination(last_page=len(db_list)))


async def current_page_error(cb: types.CallbackQuery):
    await cb.answer(cache_time=60)


async def show_current_task(cb: types.CallbackQuery, cb_data: dict):
    token = load_config().tg_bot.token
    current_task = int(cb_data.get("page"))
    text = get_task(page=current_task, user_id=cb.from_user.id)
    text = [
            f"Name: {text[2]}",
            f"Description: {text[3]}",
            f"Timezone: {text[4]}",
            f"Datetime: {text[5]}",
            "",
            f"Task ID: {text[1]}",
            ]
    print(text)
    await Bot(token=token).edit_message_text(
            chat_id=cb.message.chat.id,
            message_id=cb.message.message_id,
            text="\n".join(text),
            reply_markup=task_pagination(
                last_page=get_task(),
                page=current_task))


def register_show_first_task(dp: Dispatcher):
    dp.register_callback_query_handler(
            show_first_task,
            text="my_tasks")


def register_current_page_error(dp: Dispatcher):
    dp.register_callback_query_handler(
            current_page_error,
            pagination_cb.filter(page="empty"))
