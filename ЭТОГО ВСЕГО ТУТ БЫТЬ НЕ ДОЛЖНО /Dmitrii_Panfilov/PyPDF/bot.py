# This model's maximum context length is 4097 tokens
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
import logging
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
from openai.error import OpenAIError

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    name = State()

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    #await Form.name.set()
    await message.reply("🤖 Hi! Send me a PDF file.")

async def process_pdf_and_question(pdf_path: str, user_question: str) -> str:
    # Extract the text
    pdf_reader = PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    # Split into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # Create embeddings
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    
    # Perform similarity search
    docs = knowledge_base.similarity_search(user_question)
    
    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")
    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=user_question)
    return response

@dp.message_handler(lambda message: message.text and not message.text.startswith('/'), state='*')
async def process_question(message: types.Message, state: FSMContext):
    user_question = message.text  # просто текст сообщения
    async with state.proxy() as data:
        pdf_path = data.get('pdf_path')
        if not pdf_path:
            await message.reply("🤖 First, upload a PDF file‼️")
            return
        try:
            response = await process_pdf_and_question(pdf_path, user_question)
            await message.reply(f"💡 Answer:\n{response}")
        except Exception as e:  # Здесь ловим все исключения, например, превышение длины текста
            await message.reply(f"‼️ An error occurred:‼️\n{e}")


@dp.message_handler(content_types=['document'], state='*')
async def process_pdf(message: types.Message, state: FSMContext):
    pdf_path = f"{message.document.file_id}.pdf"
    await bot.download_file_by_id(message.document.file_id, destination=pdf_path)
    await state.update_data(pdf_path=pdf_path)
    await message.reply("🤖 PDF received! Send me a question...")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
