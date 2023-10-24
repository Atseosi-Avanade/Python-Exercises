import imdb

ia = imdb.IMDb()

for rank, movie in enumerate(ia.get_top250_movies(), start=1):
    if len(str(movie)) == 10:
        print(f"{rank:>4d}: {movie}")




