import imdb
import re
import sys
import mytimer
import threading

ia = imdb.IMDb()


def get_online(pattern):
    """ Get top 250 movies online and measure time. """
    start_time = mytimer.start_timer()
    for rank, movie in enumerate(ia.get_top250_movies(), start=1):
        m = re.search(pattern, str(movie), re.IGNORECASE)
        if m:
            print(f"{rank:>4d}: {movie}")
    mytimer.end_timer(start_time, "T1 elapsed time: ")
    return None

def get_local(pattern):
    """ Get top 250 movies online and measure time. """
    start_time = mytimer.start_timer()
    with open(r"top250_movies.txt", mode="rt") as fh_in:
        for rank, movie in enumerate(fh_in, start=1):
            m = re.search(pattern, str(movie), re.IGNORECASE)
            if m:
                print(f"{rank:>4d}: {movie}", end="")
    mytimer.end_timer(start_time, "T2 elapsed time: ")
    return None

def main():
    """ Main program """
    pattern = input("Enter movie name: ")

    t1 = threading.Thread(target=get_online, args=(pattern,))
    t2 = threading.Thread(target=get_local, args=(pattern,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)