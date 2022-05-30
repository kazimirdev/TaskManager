from aiogram import types, Dispatcher

from tgbot.keyboards.back_to_main_menu_keyboard import back_to_main_menu_keyboard


async def faq(cb: types.CallbackQuery):
    text = [
            "FAQ:",
            "Q: How long does bot keep tasks?",
            "A; It stores tasks up to the year 9999",
            "",
            "Q: Who has access to information?",
            "A: Only the user who created the task and the author of the project",
            "",
            "Q: I don't want to share my plans with the autor who has created this program!",
            "A: You can create your own bot based on the source code.",
            "",
            "Q: How does the author make money on this project?",
            "A: This project is full non-commenrce.",
            "",
            "Q: How can I help the autor?",
            "A: You can share link to this bot.",
            "A: You can star a project on GitHub.",
            "A: You can make a money transfer:",
            "A: BTC - <code>3NqNL4yfSgLftJtjbEQj4rAq89ouWx2sRy</code>",
            "A: ETH (ERC20) - <code>0xad237da7905e41feaf017d7f02f0f5b49e422d7d</code>",
            "A: DOGE - <code>DD5MuSspktUhbZYTxXG9TPZUUZwncZqBWo</code>",
            "A: USDT (TRC20) - <code>TVeY9rdttNSP7iM63tdKEy6KL5Su5deNEs</code>",
            "A: USDT (ERC20) - <code>0x61b75c86bdd5dd2a7ad6aff74839c9645ff2ae1f</code>",
            "A: SHIB (ERC20) - <code>0xad237da7905e41feaf017d7f02f0f5b49e422d7d</code>"
            ]
    await cb.message.edit_text(
            text="\n".join(text),
            reply_markup=back_to_main_menu_keyboard
            )


def register_faq(dp: Dispatcher):
    dp.register_callback_query_handler(
            faq,
            text="faq"
            )
