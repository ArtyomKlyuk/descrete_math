def get_permutation(n, k):
    i = k - 1
    perm = [0 for i in range(k)]
    while i != -1:
        print(perm)
        i = k - 1
        while perm[i] > n - 1 and i != -1:
            i -= 1
        perm[i] += 1
        for j in range(i + 1, k):
            perm[j] = 0


get_permutation(5, 3)
