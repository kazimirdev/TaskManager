from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main_menu_keyboard = InlineKeyboardMarkup(
        row_width=3,
        inline_keyboard=[
            [
            InlineKeyboardButton(
                text="New task",
                callback_data="new_task")],
            [
            InlineKeyboardButton(
                text="My tasks",
                callback_data="my_tasks")],
            [
            InlineKeyboardButton(
                text="FAQ",
                callback_data="faq"),
            InlineKeyboardButton(
                text="Sourse code",
                url="https://github.com/Greenboyisyourdream/TaskManager"
                )]])
