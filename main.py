import asyncio
from aiogram import Bot, Dispatcher
from docs import token

bot = Bot(token=token)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

print(0)