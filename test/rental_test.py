import unittest

from approvaltests.approvals import verify
from approvaltests.reporters.generic_diff_reporter import GenericDiffReporter

from src.customer import Customer
from src.movierental import MovieRental
from src.rentalinfo import RentalInfo


class Tests(unittest.TestCase):
    def setUp(self):
        self.reporter = GenericDiffReporter(("Tortoise", "C:/Program Files/TortoiseSVN/bin/tortoisemerge.exe"))

    def test_it_should_return_the_proper_result(self):
        customer = Customer("martin", [MovieRental("F001", 3), MovieRental("F002", 1)])
        verify(RentalInfo().statement(customer), self.reporter)
