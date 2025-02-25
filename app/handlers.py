from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)
    await message.reply('Как дела?')

@router.message(Command('help'))
async def help(message: Message):
    await message.answer(f'Возможные команды:\n1. /start - перезапуск бота\n2. /help - список команд')

@router.message(F.text == 'GG')
async def test(message: Message):
    await message.reply('Как дела?')