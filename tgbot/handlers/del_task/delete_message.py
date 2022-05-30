from aiogram import types, Dispatcher


async def del_message(cb: types.CallbackQuery):
    await cb.answer()
    await cb.message.delete()


def register_del_message(dp: Dispatcher):
    dp.register_callback_query_handler(
            del_message,
            text="del_message")
