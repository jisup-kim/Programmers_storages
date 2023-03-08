def solution(survey, choices):
    check_ch = ["R","T","C","F","J","M","A","N"]
    check_count = [0] * 8
    result = ""
    
    print(result)
    for index,ch in enumerate(survey):
        left_ch, right_ch = ch[0] , ch[1]
        
        if choices[index] < 4:
            check_count[check_ch.index(left_ch)] += (4-choices[index])
        else:
            if left_ch in ("R","C","J","A"):
                check_count[check_ch.index(left_ch)+1] += (choices[index]-4)
            else:
                check_count[check_ch.index(left_ch)-1] += (choices[index]-4)
    for n in range(0,7,2):
        if check_count[n] >= check_count[n+1]:
            result += check_ch[n]
        else:
            result += check_ch[n+1]
    return result
    