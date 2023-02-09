N = int(input("Введите количество элементов в массиве: "))
lst_1 = []
for i in range(1, N + 1):
    lst_1.append(i)
print(lst_1)
x = int(input("Введите число, которое хотите проверить: "))
for i in range(1, N + 1):
    if i == x:
        count = x - 1
print(count)