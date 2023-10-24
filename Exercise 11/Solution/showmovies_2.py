import movie

def main():
    first_movie = movie.Movie()
    first_movie.title = "Jaws"
    first_movie.director = "Steven Spielberg"
    first_movie.year = 1975
    first_movie.display_details()

    second_movie = movie.Movie()
    second_movie.title = "Vanilla Sky"
    second_movie.director = "Cameron Crowe"
    second_movie.year = 1986
    second_movie.display_details()
    return None

if __name__ == "__main__":
    main()
