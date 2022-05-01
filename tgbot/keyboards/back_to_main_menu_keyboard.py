from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


back_to_main_menu_keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[[InlineKeyboardButton(
            text="Main menu",
            callback_data="main_menu")]]
        )
