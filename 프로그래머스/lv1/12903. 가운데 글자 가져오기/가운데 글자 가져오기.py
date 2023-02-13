def solution(s):
    check_point = int(len(s)//2)
    
    if (len(s)%2) == 0:
        answer = s[check_point-1]+s[check_point]
    else:
        answer = s[check_point]
    return answer