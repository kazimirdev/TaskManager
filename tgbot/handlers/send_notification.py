import sqlite3

from aiogram import types, Bot, Dispatcher


async def send_notification():
    db = sqlite3.connect("db/main.db").cursor()
    db.execute("select * from tasks where sent = False and server_time < now()")
    
