import imdb

ia = imdb.IMDb()

movies10 = { rank: str(movie) for rank, movie in
             enumerate(ia.get_top250_movies(),start=1)
             if len(str(movie)) == 10 }

for rank, film in movies10.items():
    print(f"{rank:>4d}: {film}")





