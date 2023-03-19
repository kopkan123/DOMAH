N = int(input('Введите кол-во элементов в масиве:'))
X = int(input('Введите число которое необхадимо проверить:'))
count = 0
for i in range(N):
    if i == X:
        count += 1
        print(range(N))
print(f'Число {X} встречается {count} раз')
