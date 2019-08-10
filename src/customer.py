class Customer(object):
    name: str
    rentals: list

    def __init__(self, name, rentals):
        self.name = name
        self.rentals = rentals
