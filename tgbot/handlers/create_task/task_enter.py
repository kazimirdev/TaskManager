from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext

from tgbot.keyboards.back_to_main_menu_keyboard import (
        back_to_main_menu_keyboard
        )
from tgbot.states import NewTaskState


async def task_enter(cb: types.CallbackQuery, state: FSMContext):
    await cb.answer()
    text = "Write the name of the task:"
    await cb.message.edit_text(
            text=text,
            reply_markup=back_to_main_menu_keyboard
            )
    await NewTaskState.first()
    await state.update_data(
            {
                "name_id": cb.message.message_id
                }
            )
    await NewTaskState.Name.set()


def register_task_enter(dp: Dispatcher):
    dp.register_callback_query_handler(
            task_enter,
            text="new_task",
            state="*"
            )
