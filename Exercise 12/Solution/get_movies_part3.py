import imdb
import mytimer
import sys

ia = imdb.IMDb()
start_time = None
# start_time = mytimer.start_timer()

for rank, movie in enumerate(ia.get_top250_movies(), start=1):
    print(f"{rank:>4d}: {movie}")

try:
    mytimer.end_timer(start_time)
except SystemError as err:
    print("End timer error -", err, file=sys.stderr)
