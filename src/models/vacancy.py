class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = self.validate_salary(salary)
        self.description = description

    def validate_salary(self, salary):
        if salary is None:
            return "Зарплата не указана"
        return salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    @staticmethod
    def cast_to_object_list(vacancies_json):
        return [Vacancy(item['name'], item['alternate_url'], item['salary'], item['snippet']['requirement']) for item in vacancies_json]