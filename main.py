import asyncio

from aiogram import Bot, Dispatcher

from handlers import router

from config import TOKEN

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_router(router)
                      

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())