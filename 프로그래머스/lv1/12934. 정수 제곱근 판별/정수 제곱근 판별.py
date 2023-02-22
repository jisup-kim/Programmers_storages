def solution(n):
    n_sqrt = n ** (1/2)
    if n_sqrt % 1 == 0:
        result = (n_sqrt+1)**2
    else:
        result = -1
    return (result)