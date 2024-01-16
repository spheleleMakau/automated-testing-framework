import unittest
from framework.web_driver import WebDriver

class TestExample(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()

    def tearDown(self):
        self.driver.close()

    def test_google_search(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.driver.title)

