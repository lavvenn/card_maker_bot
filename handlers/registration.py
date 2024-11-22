from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.context import FSMContext

from keyboards.reply import main_kb, cancel_kb
from keyboards.inline import course_select_kb, confirmation_kb

from bot_states import Registration

router = Router()


@router.message(F.text == "📝 отпрвить данные на пропуск")
async def registration_start(message: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer("напишите ваши имя и фамилию", reply_markup=cancel_kb)

@router.message(Registration.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.course)
    await message.answer("выберите курс", reply_markup=course_select_kb)

@router.callback_query(Registration.course)
async def process_course(callback: CallbackQuery, state: FSMContext):
    await state.update_data(course=callback.data)
    await state.set_state(Registration.photo)
    await callback.message.delete()
    await callback.message.answer("пришлите фото")

@router.message(Registration.photo)
async def process_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await state.set_state(Registration.confirmation)
    data = await state.get_data()
    await message.delete()
    await message.answer_photo( photo=data['photo'], caption=f"""
                           имя фамилия: {data['name']}
                           курс: {data['course']}

                           """, reply_markup=confirmation_kb)

@router.callback_query(Registration.confirmation)
async def process_confirmation(callback: CallbackQuery, state: FSMContext, bot: Bot):

    if callback.data == "yes":
        data = await state.get_data()

        photo_info = await bot.get_file(data['photo'])
        await bot.download_file(photo_info.file_path, f"photos/{data['name'].split()[0]}.jpg")
        await callback.message.answer("вы успешно зарегистрировались", reply_markup=main_kb)
        await state.clear()
        await callback.message.delete()
    else:
        await callback.message.answer("вы отменили регистрацию", reply_markup=main_kb)
        await state.clear()


