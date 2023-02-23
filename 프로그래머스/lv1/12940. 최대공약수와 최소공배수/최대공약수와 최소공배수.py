def solution(n, m):
    n_list = []
    result = []
    
    for i in range(1, n+1):
        if n % i == 0:
            n_list.append(i)
            
    for x in n_list[::-1]:
        if m % x == 0:
            result.append(x)
            break
            
    x_mul = 1
    while len(result) < 2:
        if (m * x_mul) % n == 0:
            result.append(m*x_mul)
        else:
            x_mul += 1
    return result
