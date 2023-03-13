def solution(s):
    array = []
    s_min = 99999999999
    s_max = -99999999999
    
    array.append(list(map(int, s.split())))
    
    for x in array[0]:
        s_min = min(s_min, x)
        s_max = max(s_max, x)
    print(s_min, s_max)
    answer = str(s_min) + " " + str(s_max)
    return answer