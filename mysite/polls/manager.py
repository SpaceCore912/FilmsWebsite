import json,csv
from .views import Film
def filmloader():
    with open("polls/test.json",encoding="utf-8") as f:
        json_data=json.load(f)
        for movie_data in json_data:
            movie=Film.create(**movie_data)
    return None
def filmloader1():
    with open("polls/famous-movies.json",encoding="utf-8") as q:
        json_data=json.load(q)
        for movie_data in json_data:
            movie=Film.create(**movie_data)
    return None