import pytest
import os
from src.models.vacancy import Vacancy
from src.storage.json_saver import JSONSaver

def test_add_vacancy():
    vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/123", "100000-150000 руб.", "Требования: Python, Django")
    saver = JSONSaver("test_vacancies.json")
    saver.add_vacancy(vacancy)
    with open("data/test_vacancies.json", "r") as file:
        data = json.load(file)
        assert vacancy.__dict__ in data
    os.remove("data/test_vacancies.json")