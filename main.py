import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import Config, load_config
from keyboards.set_menu import set_main_menu
from handlers import hd_common


def logger_init():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %Z'
    )

    return logging.getLogger(__name__)


async def on_startup(bot: Bot):
    await set_main_menu(bot)
    # await bot.send_message(config.admin_id, text='Бот запущен!')

async def on_shutdown(bot: Bot):
    # await bot.send_message(config.admin_id, text='Бот остановлен!')
    pass


async def main() -> None:
    logger = logger_init()
    logger.info('Starting bot')

    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    bot.default.parse_mode = ParseMode.HTML
    dp = Dispatcher()

    # On startup and shutdown
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    # Include routers
    dp.include_routers(hd_common.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())