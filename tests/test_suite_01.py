import unittest
from tests.scenario01.result_list_tests_csv_data import CSVDataLoginTests
from tests.scenario01.result_list_tests_multiple_data import MultipleDataLoginTests

# Get all tests from test classes
tc1 =unittest.TestLoader().loadTestsFromTestCase(CSVDataLoginTests)
tc2 =unittest.TestLoader().loadTestsFromTestCase(MultipleDataLoginTests)

# Create a test suite combining all test classes
smokeTest=unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)