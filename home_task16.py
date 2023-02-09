N = int(input("Введите количество элементов в массиве: "))
lst_1 = []
for i in range(1, N):
    lst_1.append(i)
print(lst_1)
x = int(input("Введите число, которое хотите проверить: "))
count = 0
for i in range(1, N):
    if i == x:
        count += 1
print(count)