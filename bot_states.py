from aiogram.fsm.state import StatesGroup, State

class Registration(StatesGroup):

    course = State()
    name = State()
    photo = State()

    confirmation = State()