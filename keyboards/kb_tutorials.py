from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_TUTORIALS_KB_RU


def create_tutorials_keyboard() -> InlineKeyboardMarkup:
    """
    Функция создает клавиатуру с темами для обучения
    :return: Клавиатура с темами для обучения
    """
    keyboard = InlineKeyboardMarkup(row_width=1)
    for key, value in LEXICON_TUTORIALS_KB_RU.items():
        keyboard.insert(InlineKeyboardButton(text=value, callback_data=key))
    return keyboard