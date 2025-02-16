from src.models.vacancy import Vacancy

def test_vacancy_creation():
    vacancy = Vacancy("Python Developer", "https://example.com", 100000, "Описание Python")
    assert vacancy.title == "Python Developer"
    assert vacancy.salary == 100000