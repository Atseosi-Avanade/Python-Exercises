import imdb
import re

ia = imdb.IMDb()

pattern = input("Enter movie name: ")
reobj = re.compile(pattern, re.IGNORECASE)  # Pre-compile pattern before loop.

for rank, movie in enumerate(ia.get_top250_movies(), start=1):
    m = reobj.search(str(movie))
    if m:
        print(f"{rank:>4d}: {movie}")

