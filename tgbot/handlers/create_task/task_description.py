from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext

from tgbot.config import load_config
from tgbot.keyboards.back_to_main_menu_keyboard import (
        back_to_main_menu_keyboard)
from tgbot.states import NewTaskState


async def task_description(message: types.Message, state: FSMContext):
    await state.update_data({"answer_description": message.text})
    token = load_config(".env").tg_bot.token
    data = await state.get_data()
    text = [
            "Write city from your timezone:",
            " ",
            f"Name: {data.get('answer_name')}",
            f"Description: {data.get('answer_description')}",
            "Timezone: "
            ]
    await Bot(token=token).edit_message_text(
            chat_id=message.chat.id,
            message_id=data.get("name_id"),
            text="\n".join(text),
            reply_markup=back_to_main_menu_keyboard
            )
    await message.delete()
    await NewTaskState.Region.set()


def register_task_description(dp: Dispatcher):
    dp.register_message_handler(
            task_description,
            state=NewTaskState.Description
            )
