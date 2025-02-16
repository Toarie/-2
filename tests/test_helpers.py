from src.utils.helpers import filter_vacancies, sort_vacancies
from src.models.vacancy import Vacancy

def test_filter_vacancies():
    vacancies = [
        Vacancy("Python Developer", "https://example.com", 100000, "Описание Python"),
        Vacancy("Java Developer", "https://example.com", 90000, "Описание Java"),
    ]
    filtered = filter_vacancies(vacancies, ["Python"])
    assert len(filtered) == 1
    assert filtered[0].title == "Python Developer"

def test_sort_vacancies():
    vacancies = [
        Vacancy("Python Developer", "https://example.com", 100000, "Описание Python"),
        Vacancy("Java Developer", "https://example.com", 90000, "Описание Java"),
    ]
    sorted_vacancies = sort_vacancies(vacancies)
    assert sorted_vacancies[0].salary == 100000