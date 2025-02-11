import pytest
from src.models.vacancy import Vacancy
from src.utils.helpers import filter_vacancies, sort_vacancies

def test_filter_vacancies():
    vacancies = [
        Vacancy("Python Developer", "https://hh.ru/vacancy/1", "100000", "Требования: Python, Django"),
        Vacancy("Java Developer", "https://hh.ru/vacancy/2", "120000", "Требования: Java, Spring")
    ]
    filtered = filter_vacancies(vacancies, ["Python"])
    assert len(filtered) == 1
    assert filtered[0].title == "Python Developer"

def test_sort_vacancies():
    vacancies = [
        Vacancy("Python Developer", "https://hh.ru/vacancy/1", "100000", "Требования: Python"),
        Vacancy("Java Developer", "https://hh.ru/vacancy/2", "120000", "Требования: Java")
    ]
    sorted_vacancies = sort_vacancies(vacancies)
    assert sorted_vacancies[0].title == "Java Developer"