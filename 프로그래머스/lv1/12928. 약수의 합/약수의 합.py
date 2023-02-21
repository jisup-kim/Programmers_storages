def solution(n):
    sum = 0
    
    for x in range(1,n+1):
        if n%x == 0:
            sum += x
    return sum