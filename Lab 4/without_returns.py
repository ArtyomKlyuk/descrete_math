sequince = [0, 1, 2, 3, 4]


def reverse(sequince, index):
    shift = index + 1
    n = len(sequince)
    for i in range((n - shift) // 2):
        sequince[shift + i], sequince[n - 1 - i] = sequince[n - 1 - i], sequince[shift + i]


def k_permutaion_of_n(k, sequince):
    n = len(sequince)
    for j in range(k, n):
        if sequince[j] > sequince[k - 1]:
            break
    else:
        j = n
    if j < n:
        sequince[k - 1], sequince[j] = sequince[j], sequince[k - 1]
        return sequince[:k:]
    else:
        reverse(sequince, k - 1)
        for i in range(k - 2, -1, -1):
            if sequince[i] < sequince[i + 1]:
                break
        else:
            return None
        for j in range(n - 1, i, -1):
            if sequince[j] > sequince[i]:
                break
        sequince[i], sequince[j] = sequince[j], sequince[i]
        reverse(sequince, i)
        return sequince[:k:]


k = 5
perm = sequince[:k]
while perm is not None:
    print(perm)
    perm = k_permutaion_of_n(k, sequince)
