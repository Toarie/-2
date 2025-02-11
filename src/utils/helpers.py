def filter_vacancies(vacancies, filter_words):
    return [vacancy for vacancy in vacancies if any(word in vacancy.description for word in filter_words)]

def sort_vacancies(vacancies):
    return sorted(vacancies, reverse=True)