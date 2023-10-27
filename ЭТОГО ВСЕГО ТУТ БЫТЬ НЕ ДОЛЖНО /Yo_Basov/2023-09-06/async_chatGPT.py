from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import openai
import os


load_dotenv()

TOKEN = os.environ.get("TOKEN")
GPT_SECRET_KEY = os.environ.get("GPT_SECRET_KEY")

openai.api_key = GPT_SECRET_KEY


async def get_answer(text):
    completion = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo-0301",
        messages=[{"role": "user", "content": text}])
    return completion.choices[0].message["content"]


async def start(update, context):
    await update.message.reply_text('Задайте любой вопрос chatGPT')


async def help_command(update, context):
    await update.message.reply_text("Вы можете пообщаться с chatGPT на любую тему")


async def gpt(update, context):
    res = await get_answer(update.message.text)
    await update.message.reply_text(res)


def main():

    application = Application.builder().token(TOKEN).build()
    print('Бот запущен...')

    application.add_handler(CommandHandler("start", start, block=False))
    application.add_handler(CommandHandler("help", help_command, block=False))
    application.add_handler(MessageHandler(filters.TEXT, gpt, block=False))

    # запуск приложения. Для остановки нужно нажать Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()