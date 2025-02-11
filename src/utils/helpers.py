from typing import List
from src.models.vacancy import Vacancy

def filter_vacancies(vacancies: List[Vacancy], filter_words: List[str]) -> List[Vacancy]:
    """
    Фильтрует список вакансий по ключевым словам в описании.

    :param vacancies: Список вакансий.
    :param filter_words: Список ключевых слов для фильтрации.
    :return: Отфильтрованный список вакансий.
    """
    return [vacancy for vacancy in vacancies if any(word.lower() in vacancy.description.lower() for word in filter_words)]

def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """
    Сортирует список вакансий. По умолчанию сортирует по убыванию (например, по зарплате или дате).

    :param vacancies: Список вакансий.
    :return: Отсортированный список вакансий.
    """
    # Пример сортировки по зарплате (предполагается, что salary является числом или имеет метод сравнения)
    return sorted(vacancies, key=lambda x: x.salary, reverse=True)