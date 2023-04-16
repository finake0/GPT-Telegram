import openai
from aiogram import Bot, Dispatcher, types
from aiogram.types.message import ContentType
from aiogram.utils import executor

openai.api_key = "" #openai

bot = Bot(token="") #@BotFather
dp = Dispatcher(bot)


def generate_response(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет!")


@dp.message_handler(content_types=ContentType.ANY)
async def generate_answer(message: types.Message):
    question = message.text
    answer = generate_response(question)
    await message.answer(answer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
