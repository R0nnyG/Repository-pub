ticket = int(input("Количество необходимых билетов: "))
price = []
for i in range(1, ticket + 1):
    age = int(input(f"Возраст {i} гостя? "))
    if age < 18:
        price.append(0)
    elif 18 <= age <= 24:
        price.append(990)
    elif 25 <= age:
        price.append(1390)
if ticket >= 3:
    discount = int(sum(price) - sum(price)/10)
    print("Стоимость билетов со скидкой: ", discount)
else:
    full_price = sum(price)
    print("Стоимость билетов: ", full_price)
