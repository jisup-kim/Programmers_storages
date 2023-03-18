def solution(n):
    result = 0
    INF = int(1e9)
    n_bin_1 = bin(n)[2:].count("1")

    for i in range(n+1, INF):
        i_bin_1 = bin(i)[2:].count("1")
        if n_bin_1 == i_bin_1:
            result = i
            break
    return result