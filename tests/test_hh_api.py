from src.api.hh_api import HeadHunterAPI

def test_get_vacancies():
    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies("Python")
    assert isinstance(vacancies, list)