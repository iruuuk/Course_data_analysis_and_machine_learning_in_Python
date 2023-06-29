#кейс 1
ill = [3900, 4400, 4300, 4600, 4700]
deth = [900, 997, 1001, 1003, 987]
procent = []
for i in list(zip(deth, ill)):
    dolya = (i[0]/i[1]) * 100
    procent.append(dolya)
print(procent, '%')
sred = 0
for i in ill:
    sred += i
print(sred/5)
sreddeath = 0
for j in deth:
    sreddeath += j
print(sreddeath/5)

#кейс 2
employees = ['Иванов', 'Рогов', 'Александров', 'Зайцев', 'Булкин', 'Прохоров']
print(' В этот день было ', len(employees), ' сотрудников')
surname = input('Введите фамилию: ')
m = 0
for i in employees:
    if surname == i:
        print('Был')
        m = 0
        break
if m == 1:
    print('Не был')

#кейс 3
medicines = ['Спазмалгон', 'Нурофен', 'Тизин', 'Назонекс', 'Грипферон', 'Боярышник']
price = [300, 500, 124, 750, 567, 320]
times = [10, 6, 12, 4, 5, 20]
purchases = list(zip(medicines, price, times))
i = 0
def avg_purchases():
    avgpurchases = 0
    for i in times:
        avgpurchases += i
    print(avgpurchases/6)
avg_purchases()
def profit():
    full_profit = 0
    for i in range(0, 6):
        full_profit += price[i] * times[i]
    print(full_profit)
profit()
def prices():
    print(list(zip(medicines, price)))
prices()
def maximum():
    max_element = max(price)
    print(max_element)
maximum()
def minimum():
    min_element = min(price)
    print(min_element)
minimum()
def avg_price():
    avgprice = 0
    for i in price:
        avgprice += i
    print(avgprice/6)
avg_price()
func = int(input('Выберите значение, которое нужно посчитать: \
                 1 - средние данные о продажах; \
                 2 - данные о выручке, \
                 3 - данные о ценах, \
                 4 - максимальная цена лекарства, \
                 5 - минимальная цена лекарства, \
                 6 - средняя цена лекарств. '))
if func == 1:
    avg_purchases()
elif func == 2:
    profit()
elif func == 3:
    prices()
elif func == 4:
    maximum()
elif func == 5:
    minimum()
elif func == 6:
    avg_price()
else:
    print('Такого значения не существует')
