import requests
from typing import List, Dict

class HeadHunterAPI:
    __slots__ = ['__base_url']

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"

    def __connect_to_api(self, params: Dict) -> Dict:
        """
        Подключается к API и возвращает ответ.
        """
        response = requests.get(self.__base_url, params=params)
        response.raise_for_status()  # Проверка статус-кода
        return response.json()

    def get_vacancies(self, search_query: str) -> List[Dict]:
        """
        Получает вакансии по запросу.
        """
        params = {"text": search_query}
        return self.__connect_to_api(params).get("items", [])