from src.storage.json_saver import JSONSaver
from src.models.vacancy import Vacancy

def test_add_vacancy():
    saver = JSONSaver("test_vacancies.json")
    vacancy = Vacancy("Python Developer", "https://example.com", 100000, "Описание Python")
    saver.add_vacancy(vacancy)
    assert len(saver.load_vacancies()) == 1