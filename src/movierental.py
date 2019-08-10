class MovieRental(object):
    movie_id: str
    days: int

    def __init__(self, movie_id, code):
        self.movie_id = movie_id
        self.days = code
