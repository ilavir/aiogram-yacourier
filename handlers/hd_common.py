import logging
import time
import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, or_f

from keyboards.kb_common import create_main_keyboard, create_register_keyboard, create_faq_keyboard
from lexicon.lexicon_ru import LEXICON_RU, LEXICON_COMMANDS_RU, LEXICON_FAQ_RU


logger = logging.getLogger(__name__)

router = Router()


@router.message(CommandStart())
# async def cmd_start(message: Message, request: DbRequest):
    # await request.save_user(message.from_user.id, message.from_user.is_bot, message.from_user.first_name, message.from_user.last_name, message.from_user.full_name,
    #                         message.from_user.username, message.from_user.language_code, message.from_user.is_premium if message.from_user.is_premium else False)
async def cmd_start(message: Message):
    await message.answer(LEXICON_RU['/start_1'])
    time.sleep(2)
    await message.answer(LEXICON_RU['/start_2'], reply_markup=create_main_keyboard())
    time.sleep(3)
    await message.answer(LEXICON_RU['/register'], reply_markup=create_register_keyboard())


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(LEXICON_RU[message.text])


@router.message(or_f(Command('register'), F.text == LEXICON_COMMANDS_RU.get('/register')))
async def cmd_register(message: Message):
    await message.answer(LEXICON_RU['/register'], reply_markup=create_register_keyboard())


@router.message(or_f(Command('faq'), F.text == LEXICON_COMMANDS_RU.get('/faq')))
async def cmd_faq(message: Message):
    await message.answer(LEXICON_RU.get('/faq'), reply_markup=create_faq_keyboard())


@router.callback_query(F.data.startswith('faq_'))
async def faq_questions(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_FAQ_RU[callback.data], reply_markup=callback.message.reply_markup)


@router.message(or_f(Command('tutorials'), F.text == LEXICON_COMMANDS_RU.get('/tutorials')))
async def cmd_tutorials(message: Message):
    await message.answer(LEXICON_RU.get('/tutorials'))


@router.message()
async def no_handled(message: Message):
    await message.answer(LEXICON_RU['no_handled'])
