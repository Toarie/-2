from api.hh_api import HeadHunterAPI
from models.vacancy import Vacancy
from storage.json_saver import JSONSaver

def user_interaction():
    hh_api = HeadHunterAPI()
    json_saver = JSONSaver()

    search_query = input("Введите поисковый запрос: ")
    vacancies_json = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(vacancies_json)

    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    filtered_vacancies = [vacancy for vacancy in vacancies_list if any(word in vacancy.description for word in filter_words)]
    sorted_vacancies = sorted(filtered_vacancies, reverse=True)
    top_vacancies = sorted_vacancies[:top_n]

    for vacancy in top_vacancies:
        print(f"{vacancy.title} - {vacancy.salary} - {vacancy.link}")

if __name__ == "__main__":
    user_interaction()