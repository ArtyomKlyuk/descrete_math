def combinations(c, n):
    comb = [*range(c), n, 0]
    j = 0
    while j < c:
        print(*comb[:c])
        j = 0
        while comb[j] + 1 == comb[j + 1] and j != len(comb):
            comb[j] = j
            j += 1
        comb[j] += 1

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
combinations(a, b)
input()
