from src.customer import Customer
from src.movie import Movie


class RentalInfo(object):
    def __init__(self):
        pass

    def statement(self, customer: Customer):
        total_amount = 0
        frequent_renter_points = 0
        result = f"Rental Record for {customer.name}\n"
        for r in customer.rentals:
            movie = self.lookup_movie(r.movie_id)

            # determine amount for each movie
            this_amount = 0

            if movie.code == "regular":
                this_amount = 2
                if r.days > 2:
                    this_amount += (r.days - 2) * 1.5
            elif movie.code == "new":
                this_amount = r.days * 3
            elif movie.code == "childrens":
                this_amount = 1.5
                if r.days > 3:
                    this_amount += (r.days - 3) * 1.5

            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if movie.code == "new" and r.days > 2:
                frequent_renter_points += 1

            # print figures for this rental
            result += f"\t{movie.title}\t{this_amount}\n"
            total_amount += this_amount

        # add footer lines
        result += f"Amount owed is {total_amount}\n"
        result += f"You earned {frequent_renter_points} frequent renter points\n"
        return result

    def lookup_movie(self, movie_id):
        movies = {
                     "F001": Movie("Ran", "regular"),
                     "F002": Movie("Trois Couleurs: Bleu", "regular"),
                     "F003": Movie("Cars 2", "childrens"),
                     "F004": Movie("Latest Hit Release", "new"),
        }
        return movies[movie_id]

