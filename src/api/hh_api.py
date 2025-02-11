import requests
from abc import ABC, abstractmethod

class VacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        pass

class HeadHunterAPI(VacancyAPI):
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword):
        params = {'text': keyword, 'per_page': 100}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()['items']
        else:
            return []