from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext

from tgbot.config import load_config
from tgbot.keyboards.main_menu import main_menu_keyboard
from tgbot.services import db_check


async def main_menu(
        instance: types.CallbackQuery | types.Message,
        state: FSMContext
        ):
    await state.reset_state(with_data=True)
    text = [
            "Hi, {}!",
            "This bot is your task manager.",
            "",
            'Press "New task" for adding new task.',
            'Press "My tasks" if you want to look at your tasks.',
            'Press "FAQ" if you have some questions.',
            'Prees "Source code" if you want to "look under the hood"',
            "",
            "The author wishes you happiness in using the bot!"
            ]
    if isinstance(instance, types.CallbackQuery):
        await instance.answer()
        await instance.message.edit_text(
                text="\n".join(text[3:7]),
                reply_markup=main_menu_keyboard
                )
    if isinstance(instance, types.Message):
        db_check(load_config().db.path)
        await instance.answer(
                text="\n".join(t.format(
                    instance.from_user.full_name
                    ) for t in text),
                reply_markup=main_menu_keyboard
                )


def register_main_menu(dp: Dispatcher):
    dp.register_callback_query_handler(
            main_menu,
            text="main_menu",
            state="*")
    dp.register_message_handler(
            main_menu,
            commands=["start"],
            state="*")
