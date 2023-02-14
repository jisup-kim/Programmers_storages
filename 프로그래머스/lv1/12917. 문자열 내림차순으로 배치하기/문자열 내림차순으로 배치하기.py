def solution(s):
    array_sm = []
    array_lg = []
    answer = None
    
    for x in range(len(s)):
        if ord(s[x]) > 90:
            array_sm.append(s[x])
        else:
            array_lg.append(s[x])
    array_sm.sort(reverse = True)
    array_lg.sort(reverse = True)
    
    answer_sm = "".join(array_sm)
    answer_lg = "".join(array_lg)
    
    answer = answer_sm + answer_lg
    return answer