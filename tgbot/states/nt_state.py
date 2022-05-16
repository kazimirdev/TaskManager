from aiogram.dispatcher.filters.state import State, StatesGroup


class NewTaskState(StatesGroup):
    TicketID = State()
    Name = State()
    Description = State()
    Region = State()
    City = State()
    Date = State()
    Finish = State()
