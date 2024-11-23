from aiogram import Router

from handlers.main_handler import router as main
from handlers.registration import router as registration
from handlers.admin import router as admin

router = Router()
router.include_routers(main, registration, admin)