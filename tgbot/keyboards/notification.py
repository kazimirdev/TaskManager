from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


notification_keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Delete task",
                    callback_data="del_task"
                    ),
                InlineKeyboardButton(
                    text="Delete notification",
                    callback_data="del_message"
                    )
                ]
            ]
        )
