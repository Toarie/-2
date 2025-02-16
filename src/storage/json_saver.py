import json
from typing import List
from src.models.vacancy import Vacancy

class JSONSaver:
    __slots__ = ['__filename']

    def __init__(self, filename: str):
        self.__filename = filename

    def add_vacancy(self, vacancy: Vacancy):
        """
        Добавляет вакансию в файл, если она не дублируется.
        """
        vacancies = self.load_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
            self.save_vacancies(vacancies)

    def load_vacancies(self) -> List[Vacancy]:
        """
        Загружает вакансии из файла.
        """
        try:
            with open(self.__filename, 'r', encoding='utf-8') as file:
                return [Vacancy.from_dict(data) for data in json.load(file)]
        except FileNotFoundError:
            return []

    def save_vacancies(self, vacancies: List[Vacancy]):
        """
        Сохраняет вакансии в файл.
        """
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump([vacancy.to_dict() for vacancy in vacancies], file, ensure_ascii=False, indent=4)