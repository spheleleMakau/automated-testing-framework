import unittest
from datetime import datetime

class TestRunner:
    def __init__(self):
        self.test_suite = unittest.TestSuite()

    def add_test(self, test_case):
        self.test_suite.addTest(test_case)

    def run_tests(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_file = f"test_results_{timestamp}.txt"

        with open(result_file, "w") as result_output:
            runner = unittest.TextTestRunner(result_output)
            runner.run(self.test_suite)
