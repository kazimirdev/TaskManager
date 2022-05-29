from datetime import datetime

from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher.storage import FSMContext

from pytz import all_timezones
from tgbot.config import load_config
from tgbot.keyboards.back_to_main_menu_keyboard import (
        back_to_main_menu_keyboard
        )
from tgbot.states import NewTaskState


async def task_region(message: types.Message, state: FSMContext):
    city = "" 
    data = await state.get_data()
    text = [
            "",
            "",
            f"Name: {data.get('answer_name')}",
            f"Description: {data.get('answer_description')}",
            "",
            ]
    token = load_config(".env").tg_bot.token
    
    if " " in message.text:
        parts_c = message.text.split(" ")
        parts_c = [p.capitalize() for p in parts_c]
        city = "_".join(parts_c)
    else:
        city = message.text.capitalize()
    
    temp_city = city[:]

    for zone in all_timezones:
        if city in zone:
            city = zone
            break
    
    if city == temp_city:
        text[0] = "Write city from your timezone:"
        text[-1] = "Timezone: I don't know this region, try again"
    else:
        example = datetime.now().strftime("%Y-%m-%d %H:%M")
        await state.update_data({"answer_timezone": city})
        text[0] = f"Write the datetime (For example: {example}) when I'll send you notification:"
        text[-1] = f"Timezone: {city}"
        text.append("Date:")
        await NewTaskState.Date.set()
        
    await Bot(token=token).edit_message_text(
                    chat_id=message.chat.id,
                    message_id=data.get("name_id"),
                    text="\n".join(text),
                    reply_markup=back_to_main_menu_keyboard
                    )
    await message.delete()


def register_task_region(dp: Dispatcher):
    dp.register_message_handler(
            task_region,
            state=NewTaskState.Region
            )
