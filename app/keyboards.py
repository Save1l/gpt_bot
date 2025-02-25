from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Gpt-4o')],
                                     [KeyboardButton(text='Gpt-o1'),
                                     KeyboardButton(text='Gpt-o1 Pro')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите модель из списка...')
