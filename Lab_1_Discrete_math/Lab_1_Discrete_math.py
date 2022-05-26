def enter(x):
    n = int(input("Мощность множества: "))
    x = set()
    for i in range(n):
        x.add(input("Элемент множества: "))
    return x


a = set()
b = set()
a = enter(a)
b = enter(b)
c = a.union(b)
d = a.intersection(b)
e = a.difference(b)
f = b.difference(a)
print("Множество А: ", a)
print('Множество В: ', b)
print('Объединение: ', c)
print("Пересечение: ", d)
print('Разность A\B: ', e)
print('Разность B\A: ', f)