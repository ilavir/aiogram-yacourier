from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_BUTTONS_RU, LEXICON_MAIN_KB_RU, LEXICON_FAQ_KB_RU


def create_main_keyboard() -> ReplyKeyboardMarkup:
    register_button = KeyboardButton(text=LEXICON_MAIN_KB_RU['register_button'])
    tutorials_button = KeyboardButton(text=LEXICON_MAIN_KB_RU['tutorials_button'])
    faq_button = KeyboardButton(text=LEXICON_MAIN_KB_RU['faq_button'])

    kb_builder = ReplyKeyboardBuilder()
    kb_builder.row(register_button, faq_button, width=1)

    return kb_builder.as_markup(resize_keyboard=True)


def create_register_keyboard() -> InlineKeyboardMarkup:
    register_button = InlineKeyboardButton(text=LEXICON_BUTTONS_RU['register_button'], url=LEXICON_BUTTONS_RU['register_link'])

    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(register_button)

    return kb_builder.as_markup()


def create_faq_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=value, callback_data=key)] for key, value in LEXICON_FAQ_KB_RU.items()]
    )

    return keyboard