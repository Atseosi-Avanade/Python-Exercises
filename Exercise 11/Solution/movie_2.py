class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def display_details(self):
        print("Title:", self.title)
        print("Director:", self.director)
        print("Year:", self.year)
        return None