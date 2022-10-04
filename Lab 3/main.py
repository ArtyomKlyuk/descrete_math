def permutations(iterable):
    if len(iterable) == 1:
        # print((iterable[0],), f'Базовый случай', iterable[0])
        yield (iterable[0],)
    else:
        for perm in permutations(iterable[1:]):
            for i in range(len(iterable)):
                # print(perm[:i] + (iterable[0],) + perm[i:], f"Итерация: {i};", iterable[0], perm[:i])
                yield perm[:i] + (iterable[0],) + perm[i:]


def unique_permutations(iterable):
    return list(set(permutations(iterable)))


# first_arg = [1, 1, 1, 0]
first_arg = list(input("Введите список чисел через пробел: ").split())
second_arg = input("Введите слово: ")
# second_arg = 'миша'
print(list(map(list, unique_permutations(first_arg))))
print([''.join(x) for x in unique_permutations(second_arg)])
