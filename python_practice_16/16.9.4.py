"""Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров. Вам необходимо написать программу,
которая позволяла бы составлять список нескольких гостей. Решите задачу с помощью метода конструктора и примените один
из принципов наследования. При выводе в консоль вы должны получить: «Иван Петров, г. Москва, статус "Наставник"»'"""

# Родительский класс
class Person:
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return f'{self.name}'

# Дочерний класс
class Guest(Person):
    def __init__(self, name: str, city: str, status: str):
        super().__init__(name)
        self.city = city
        self.status = status

# Задаём формат вывода
    def __str__(self):
        return f'{self.name}, г.{self.city}, статус "{self.status}"'

# Задаём Гостей списком словарей
list_guests = [
 {"name": "Роман Дрозд", "city": "Челябинск", "status": "Руководитель отдела"},
 {"name": "Рихар Зорге", "city": "Пекин", "status": "Зарубежный поставщик"},
 {"name": "Клава Кока", "city": "Краснодар", "status": "Принеси-подай"}]

# Выводим список гостей на консоль в формате: Иван Петров, г. Москва, статус "Наставник"
print("Список гостей:")
for x in list_guests:
    print(Guest(x["name"], x["city"], x["status"].__str__()))