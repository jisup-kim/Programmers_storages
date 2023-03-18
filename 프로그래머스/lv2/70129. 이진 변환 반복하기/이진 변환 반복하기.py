def solution(s):
    zero_sum, convert_sum = 0,0 
    check_point = 0
    
    while s.count("1") > 1 or s != "1":
        one_check, zero_check = s.count("1"), s.count("0")        
        zero_sum += zero_check       
        convert_bin = bin(one_check)
        s = convert_bin[2:]
        convert_sum += 1
        check_point += 1
        
        #print("1의 갯수는 : {}, 0의 갯수는 : {}".format(one_check, zero_check))
        #print("0의 갯수 총합은 : {}, 변환된 이진수는 : {}".format(zero_sum,s))
        #print("총 변환 횟수는 : {}, while문 반복 횟수는 : {}".format(convert_sum, check_point))
    answer = [convert_sum, zero_sum]
    return answer