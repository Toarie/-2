from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Vacancy:
    title: str
    link: str
    salary: int
    description: Optional[str] = None

    def __str__(self):
        return f"{self.title} ({self.salary} руб.): {self.link}"

    @classmethod
    def from_dict(cls, data: Dict) -> 'Vacancy':
        """
        Создает объект Vacancy из словаря.
        """
        # Обработка salary
        salary_data = data.get('salary')
        if salary_data and isinstance(salary_data, dict):
            salary = salary_data.get('from') or 0
        else:
            salary = 0

        # Обработка description
        snippet = data.get('snippet', {})
        description = snippet.get('requirement') if isinstance(snippet, dict) else None

        return cls(
            title=data.get('name', 'Без названия'),
            link=data.get('alternate_url', ''),
            salary=salary,
            description=description
        )

    def to_dict(self) -> Dict:
        """
        Преобразует объект Vacancy в словарь.
        """
        return {
            "title": self.title,
            "link": self.link,
            "salary": self.salary,
            "description": self.description
        }