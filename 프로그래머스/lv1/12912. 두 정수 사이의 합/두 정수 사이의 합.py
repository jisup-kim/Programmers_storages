def solution(a, b):
    answer = 0
    
    if a == b:
        answer = a
    elif a > b:
        while True:
            if a == b:
                answer += a
                break
            answer += a
            a -= 1
    else:
        while True:
            if a == b:
                answer += b
                break
            answer += b
            b -= 1
        
    return answer