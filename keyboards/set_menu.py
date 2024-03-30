from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

from lexicon.lexicon_ru import LEXICON_COMMANDS_RU
import logging


logger = logging.getLogger(__name__)


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON_COMMANDS_RU.items()
    ]
    logger.debug(main_menu_commands)

    await bot.set_my_commands(main_menu_commands, BotCommandScopeDefault())