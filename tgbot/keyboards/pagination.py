from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


pagination_cb = CallbackData("paginator", "key", "page")


def task_pagination(last_page: int, key="my_tasks", page: int = 1):
    
    previous_page = page - 1
    previous_page_text = "<< "

    current_page_text = f"<{page}>"

    next_page = page + 1
    next_page_text = " >>"

    keyboard = InlineKeyboardMarkup(
            row_width=3,
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Main menu",
                        callback_data="main_menu"),
                    InlineKeyboardButton(
                        text="Delete task",
                        callback_data="del_task")],
                []
                ])


    if previous_page > 0:
        keyboard.insert(
                InlineKeyboardButton(
                    text=previous_page_text,
                    callback_data=pagination_cb.new(
                        key=key,
                        page=previous_page
                        )))


    keyboard.insert(
            InlineKeyboardButton(
                text=current_page_text,
                callback_data=pagination_cb.new(
                    key=key,
                    page="empty"
                    )))


    if next_page < last_page + 1:
        keyboard.insert(
                InlineKeyboardButton(
                    text=next_page_text,
                    callback_data=pagination_cb.new(
                        key=key,
                        page=next_page
                        )))


    return keyboard
