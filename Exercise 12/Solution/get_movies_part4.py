import imdb
import mytimer
import sys

ia = imdb.IMDb()
start_time = mytimer.start_timer()

try:
    for rank, movie in enumerate(ia.get_top250_movies(), start=1):
        print(f"{rank:>4d}: {movie}")
except BaseException as err:
    print("Error, count not access remote URL", err, file=sys.stderr)
    sys.exit(1)

try:
    mytimer.end_timer(start_time)
except SystemError as err:
    print("End timer error -", err, file=sys.stderr)
