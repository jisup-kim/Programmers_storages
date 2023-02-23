def solution(num):
    if num == 1:
        return 0
    
    for x in range(1,501):
        if num % 2 == 0:
            num = num / 2
            if num == 1:
                return x
        else:
            num = (num * 3)+1
            if num == 1:
                return x
    return -1
    