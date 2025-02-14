from src.api.hh_api import HeadHunterAPI
from src.storage.json_saver import JSONSaver
from src.utils.helpers import filter_vacancies, sort_vacancies
from src.models.vacancy import Vacancy

def user_interaction():
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = [Vacancy.from_dict(vacancy) for vacancy in vacancies]

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    for vacancy in sorted_vacancies[:top_n]:
        print(vacancy)

if __name__ == "__main__":
    user_interaction()