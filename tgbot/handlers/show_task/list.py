from aiogram import types, Bot, Dispatcher

from tgbot.config import load_config
from tgbot.keyboards.pagination import pagination_cb, task_pagination
from tgbot.services.get_tasks import get_task
from tgbot.services.get_len_tasks import get_len_task


async def show_first_task(cb: types.CallbackQuery):
    await cb.answer()
    token = load_config().tg_bot.token
    user_id = cb.from_user.id

    dt = get_task(user_id=user_id)
    print("--------------")
    print("User ID: ", user_id)
    print("Data from task: ", dt)
    print("--------------")

    if len(dt) == 0:
        await cb.answer(
                show_alert=True,
                text="You don't have any tasks!")
    else:
        # dt - data from taks
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
            reply_markup=task_pagination(last_page=len(dt)))


async def current_page_error(cb: types.CallbackQuery):
    await cb.answer(cache_time=60)


async def show_current_task(cb: types.CallbackQuery, callback_data: dict):
    await cb.answer()
    token = load_config().tg_bot.token
    current_task = int(callback_data.get("page"))
    user_id = cb.from_user.id
    text = get_task(page=current_task, user_id=user_id)
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
                last_page=get_len_task(user_id=user_id),
                page=current_task))


def register_show_first_task(dp: Dispatcher):
    dp.register_callback_query_handler(
            show_first_task,
            text="my_tasks")


def register_current_page_error(dp: Dispatcher):
    dp.register_callback_query_handler(
            current_page_error,
            pagination_cb.filter(page="empty"))


def register_show_current_task(dp: Dispatcher):
    dp.register_callback_query_handler(
            show_current_task,
            pagination_cb.filter(key="my_tasks"))
