from typing import List
from src.models.vacancy import Vacancy

def filter_vacancies(vacancies: List[Vacancy], filter_words: List[str]) -> List[Vacancy]:
    """
    Фильтрует вакансии по ключевым словам.
    """
    return [
        vacancy for vacancy in vacancies
        if vacancy.description and any(word in vacancy.description for word in filter_words)
    ]

def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """
    Сортирует вакансии по убыванию зарплаты.
    """
    return sorted(vacancies, key=lambda x: x.salary, reverse=True)