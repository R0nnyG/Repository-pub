""" В проекте «Дом питомца» скоро появится новая услуга: электронный кошелек. То есть система будет хранить данные о
своих клиентах и об их финансовых операциях. Написать программу, обрабатывающую данные, и на выходе в консоль
получить следующее:
Клиент "Иван Петров". Баланс: 50 руб """

# Класс Клиент-баланс
class Client:
    def __init__(self, client_name, client_balance):
        self.clientl_name = client_name
        self.client_balance = client_balance

    def get_info(self):
        return f'Клиент: "{self.clientl_name}".', \
               f'Баланс: {self.client_balance} руб'

# Клиенты "Дома питомца"
cl_1 = Client ("Гинцбург Амодей",100)
cl_2 = Client ("Соловьев Виктор",5000)
cl_3 = Client ("Ким Хэн Сук",760.7)
cl_4 = Client ("Масаеши Накатани",2500.48)

# Создадим список
clients = [cl_1, cl_2, cl_3, cl_4]

# Распечатаем список
for client in clients:
    print(*client.get_info())