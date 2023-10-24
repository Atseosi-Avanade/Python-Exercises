import imdb
import mytimer

ia = imdb.IMDb()

start_time = mytimer.start_timer()

for rank, movie in enumerate(ia.get_top250_movies(), start=1):
    print(f"{rank:>4d}: {movie}")

mytimer.end_timer(start_time)



