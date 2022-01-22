per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
money = int(input("Введите сумму вклада:"))
deposit = []
for key in per_cent:
    per_cent[key] = int(per_cent[key] * money/100)
    deposit.append(per_cent[key])
print("Доходность:", deposit)
print("Максимальная сумма, которую вы можете заработать -", max(deposit))