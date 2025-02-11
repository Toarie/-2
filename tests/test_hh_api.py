import unittest
from src.api.hh_api import HeadHunterAPI

class TestHeadHunterAPI(unittest.TestCase):
    def test_get_vacancies(self):
        api = HeadHunterAPI()
        vacancies = api.get_vacancies("Python")
        self.assertIsInstance(vacancies, list)

if __name__ == "__main__":
    unittest.main()