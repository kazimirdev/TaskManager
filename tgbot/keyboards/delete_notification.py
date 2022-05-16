from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


del_notification = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Delete Notification",
                    callback_data="del_notification"
                    )
                ]
            ]
        )
