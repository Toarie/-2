import json
import os
from abc import ABC, abstractmethod

class VacancyStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

class JSONSaver(VacancyStorage):
    def __init__(self, filename='vacancies.json'):
        self.filename = filename
        self._ensure_data_directory_exists()

    def _ensure_data_directory_exists(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        self.filename = os.path.join('data', self.filename)

    def add_vacancy(self, vacancy):
        with open(self.filename, 'a+') as file:
            file.seek(0)
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
            data.append(vacancy.__dict__)
            file.seek(0)
            json.dump(data, file, indent=4)

    def get_vacancies(self, criteria):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            return [item for item in data if criteria(item)]

    def delete_vacancy(self, vacancy):
        with open(self.filename, 'r') as file:
            data = json.load(file)
        data = [item for item in data if item != vacancy.__dict__]
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)