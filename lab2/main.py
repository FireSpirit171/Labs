import requests
import time
from googletrans import Translator
from pprint import pprint
from config import OMDB_TOKEN

URLS = {
    'search': "http://www.omdbapi.com/?i=tt3896198&apikey={}&t={}"
}

def parsing(s1):
    res = s1.split(", ")
    return res

def film_search(film, OMDB_TOKEN):
    try:
        #Создаем запрос
        r = requests.get(
            URLS['search'].format(OMDB_TOKEN, film),
        )
        data = r.json()
        #pprint(data)

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
        
        info = f"Title: {name}\nPlot: {plot}\nYear: {year}, {', '.join(country)}\nGenre: {', '.join(genre)}\nActors: {', '.join(actors)}"
        print(info)

        #Вывод на русском языке
        '''
        translator = Translator()
        info_rus = translator.translate(info, src='en', dest='ru')
        print(info_rus.text)
        '''

        [print(source, '-', rating) for source, rating in ratings.items()]
        time.sleep(5)

    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    film = input("Введите название фильма:\n")
    film_search(film, OMDB_TOKEN)

if __name__ == "__main__":
    main()