def get_permutation(n, k):
    perm = [0 for i in range(k)]
    while True:
        print(perm)
        for i in range(k-1, -1, -1):
            if perm[i] < n-1:
                break
        else:
            return
        perm[i] += 1
        for j in range(i+1, k):
            perm[j] = 0


get_permutation(5, 3)