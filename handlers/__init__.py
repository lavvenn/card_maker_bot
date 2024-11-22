from aiogram import Router

from handlers.main_handler import router as main
router = Router()
router.include_router(main)