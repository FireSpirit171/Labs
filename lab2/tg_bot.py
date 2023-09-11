import requests
import asyncio
from config import TG_BOT_TOKEN, OMDB_TOKEN
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from googletrans import Translator

URLS = {
    'search': "http://www.omdbapi.com/?i=tt3896198&apikey={}&t={}",
    'full_search': "http://www.omdbapi.com/?i=tt3896198&apikey={}&t={}&plot=full"
}

def parsing(s1):
    res = s1.split(", ")
    return res



bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == '/start')
async def start_command(message: Message):
    await message.answer("Приветствую в MovieBot! Напишите мне название фильма и я отправлю по нему всю имеющуюся информацию")

@dp.message()
async def search_film(message: Message):
    film = message.text

    try:
        #Создаем запрос
        r = requests.get(
            URLS['search'].format(OMDB_TOKEN, film),
        )
        data = r.json()

        #Получаем ключевые значения a.k.a парсим JSON
        name =  data['Title']
        year = data['Year']
        country = parsing(data['Country'])
        genre = parsing(data['Genre'])
        actors = parsing(data['Actors'])
        plot = data['Plot']
        poster = data['Poster']
        ratings = {}

        for x in data['Ratings']:
            ratings[x['Source'] if x['Source']!="Internet Movie Database" else "IMDb"] = x['Value']
        
        info = f"*****<b>{name}</b>*****\n<u>Plot</u>: {plot}\n<u>Year</u>: {year}\n<u>Country</u>: {', '.join(country)}\n<u>Genre</u>: {', '.join(genre)}\n<u>Actors</u>: {', '.join(actors)}\n****<b>RATINGS</b>****"
        for source, rating in ratings.items():
            info = info + '\n' + source + ' - ' + rating

        await message.answer_photo(photo=poster)
        await message.answer(info, parse_mode="HTML")

        #Вывод на русском языке
        '''
        translator = Translator()
        info_rus = translator.translate(info, src='en', dest='ru')
        await message.answer(info_rus.text)
        [await message.answer(source, '-', rating) for source, rating in ratings.items()]
        '''

    except:
        await message.reply("Фильм не найден. Введите другой")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
