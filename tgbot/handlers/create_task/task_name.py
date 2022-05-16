from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext

from tgbot.config import load_config
from tgbot.keyboards.back_to_main_menu_keyboard import (
        back_to_main_menu_keyboard
        )
from tgbot.states import NewTaskState


async def task_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    token = load_config(".env").tg_bot.token
    text = [
        "Write the description of the task:",
        "",
        "",
        "Description: "
        ]
    if len(message.text) <= 255:
        await state.update_data({"answer_name": message.text})
        await NewTaskState.Description.set()
        text[-2] = f"Name: {message.text}"
    else:
        text[0] = "Write the name of the task"
        text[-2] = "Name: Lenght can't be more than 256 symblols! Try again."

    await Bot(token=token).edit_message_text(
            chat_id=message.chat.id,
            message_id=data.get("name_id"),
            text="\n".join(text),
            reply_markup=back_to_main_menu_keyboard
            )
    await message.delete()


def register_task_name(dp: Dispatcher):
    dp.register_message_handler(
            task_name,
            state=NewTaskState.Name
            )
