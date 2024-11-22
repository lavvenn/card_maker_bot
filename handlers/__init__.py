from aiogram import Router

from handlers.main_handler import router as main
from handlers.registration import router as registration

router = Router()
router.include_routers(main, registration)