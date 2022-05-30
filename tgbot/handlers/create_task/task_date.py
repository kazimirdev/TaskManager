import sqlite3
from datetime import datetime

from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext

from tgbot.config import load_config
from tgbot.keyboards.back_to_main_menu_keyboard import (
        back_to_main_menu_keyboard
        )
from tgbot.services import convert_to_server_time
from tgbot.states import NewTaskState


async def task_date(
        message: types.Message,
        state: FSMContext,
        ):
    token = load_config(".env").tg_bot.token
    data = await state.get_data()
    date_example = datetime.now().strftime("%Y-%m-%d %H:%M")
    text = [
            "Write the date when I'll send you notification:",
            f"(For example: {date_example})",
            " ",
            f"Name: {data.get('answer_name')}",
            f"Description: {data.get('answer_description')}",
            f"Timezone: {data.get('answer_timezone')}",
            ""
            ]
    try:
        date, time = message.text.split(" ")
        Y, M, D = date.split("-")
        hh, mm = time.split(":")
        if str(datetime(
                year=int(Y), 
                month=int(M), 
                day=int(D), 
                hour=int(hh), 
                minute=int(mm)
                )) == message.text + ":00":
            await state.update_data({"answer_date": message.text})
            # It's adding tasks to database
            task_id = int(str(message.from_user.id) + str(message.message_id))
            name = data.get("answer_name")
            description = data.get("answer_description")
            tz = data.get("answer_timezone")
            user_date = message.text
            server_date = convert_to_server_time(
                    message.text,
                    tz,
                    "Europe/Warsaw"
                    )
            sent_status = (False if server_date > datetime.now() else None)
            db = sqlite3.connect(load_config().db.path)
            db.execute(f'insert into tasks values (?, ?, ?, ?, ?, ?, ?, ?)', 
                        (
                        int(message.from_user.id),
                        task_id,
                        name, 
                        description,
                        tz,
                        user_date,
                        server_date,
                        sent_status
                        )
                        )
            db.commit()
            db.close()
            # Tasks has beed added
            text[0] = "Successful!"
            text[1] = "I'm saving this tasks, wait please..."
            text[-1] = f"Datetime: {message.text}"
            await Bot(token=token).edit_message_text(
                    chat_id=message.chat.id,
                    message_id=data.get("name_id"),
                    text="\n".join(text),
                    reply_markup=back_to_main_menu_keyboard
                    )
            await message.delete()
            text[0] = "Task has been saved!"
            text[1] = "Press the button to return to the main menu"
            await Bot(token=token).edit_message_text(
                    chat_id=message.chat.id,
                    message_id=data.get("name_id"),
                    text="\n".join(text),
                    reply_markup=back_to_main_menu_keyboard
                    )
            await NewTaskState.Finish.set()
        else:
            raise ValueError
    except ValueError:
        text[-1] = "Datetime: Error! Try again."
        await Bot(token=token).edit_message_text(
                chat_id=message.chat.id,
                message_id=data.get("name_id"),
                text="\n".join(text),
                reply_markup=back_to_main_menu_keyboard
                )
        await message.delete()


def register_task_date(dp: Dispatcher):
    dp.register_message_handler(
            task_date,
            state=NewTaskState.Date
            )
