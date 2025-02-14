from dataclasses import dataclass
from typing import Optional

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
        salary = data.get('salary', {}).get('from') or 0
        return cls(
            title=data.get('name', ''),
            link=data.get('alternate_url', ''),
            salary=salary,
            description=data.get('snippet', {}).get('requirement', '')
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