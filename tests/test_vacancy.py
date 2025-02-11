import pytest
from src.models.vacancy import Vacancy

def test_vacancy_creation():
    vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/123", "100000-150000 руб.", "Требования: Python, Django")
    assert vacancy.title == "Python Developer"
    assert vacancy.link == "https://hh.ru/vacancy/123"
    assert vacancy.salary == "100000-150000 руб."
    assert vacancy.description == "Требования: Python, Django"

def test_validate_salary():
    vacancy = Vacancy("Developer", "https://hh.ru/vacancy/123", None, "Требования: Python")
    assert vacancy.salary == "Зарплата не указана"