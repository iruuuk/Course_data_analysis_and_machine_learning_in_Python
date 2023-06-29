spisok_1 = [2378, 2345, 334, 130, 827, 2839, 92]
m = spisok_1[0]
for i in spisok_1:
    if i < m:
        m = i
        i += 1
print(m)

a = input(str('Введите натуральное число: '))
summ = 0
for j in a:
    if (int(j) % 2 == 0):
        summ = summ + int(j)
print(summ)

spisok_2 = [8382, 492, 123, 568, 239, 2395, -21]
sum(spisok_2)
print(sum(spisok_2)/len(spisok_2))

print(max(spisok_2))
print(min(spisok_2))
print(max(spisok_2) - min(spisok_2))

spisok_3 = [378, -1328, 283, 22, -128, 1289, -128, 844, -2182]
summa = 0
for c in spisok_3:
    if c > 0:
        summa += c
print(summa)

spisok_4 = [-218, -12, -1728, 283, 2391, 1293, 203, -283]
for l in spisok_4:
    if l > 0:
        print(l)
        break

num_1 = 10
num_2 = 35
if (num_1 % 2) != 0:
    print(num_1)
else:
    print(num_2)
