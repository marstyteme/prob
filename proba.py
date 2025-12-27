from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = "8301297528:AAFgnPAgVJYaSqknjo42MkVBRZ5xmj2z7vI"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    await message.answer(f"Hello {message.from_user.first_name}!")

if __name__ == '__main__':
    executor.start_polling(dp)
