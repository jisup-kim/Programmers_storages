def solution(n):
    n_half = n // 2
    n_sum,answer,check = 0,0,1
    
    while check <= n_half:
        for i in range(check,n_half+2):
            n_sum += i
            if n_sum == n:
                answer += 1
                n_sum = 0
                break
            elif n_sum > n:
                n_sum = 0
                break
            else:
                pass
        check += 1
    return answer + 1          