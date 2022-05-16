from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#(Africa, America, Antarctica, Asia, Antlanctic, Europe, Pacific)
region_keyboard = InlineKeyboardMarkup(
        row_width=6,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Africa",
                    callback_data="Africa"),
                InlineKeyboardButton(
                    text="America",
                    callback_data="America")
                ],
            [
                InlineKeyboardButton(
                    text="Antarctica",
                    callback_data="Africa"),
                InlineKeyboardButton(
                    text="Asia",
                    callback_data="")
                ],
            [
                InlineKeyboardButton(
                    text="Australia",
                    callback_data="Africa"),
                InlineKeyboardButton(
                    text="Atlantic",
                    callback_data="")
                ],
            [
                InlineKeyboardButton(
                    text="Europe",
                    callback_data="Africa"),
                InlineKeyboardButton(
                    text="Pacific",
                    callback_data="")
                ],
            [
                InlineKeyboardButton(
                    text="-----------")
                ],
            [
                InlineKeyboardButton(
                    text="Main menu",
                    callback_data="main_menu")
                ]
            ]
        )
