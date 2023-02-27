def solution(answers):
    student_1 = [1,2,3,4,5]
    student_2 = [2,1,2,3,2,4,2,5]
    student_3 = [3,3,1,1,2,2,4,4,5,5]
    ck_number = [5,8,10]
    result = [0,0,0]
    count = [0,0,0]
    
    for i in answers:
        
        if count[0] == ck_number[0]:
            count[0] = 0
        if count[1] == ck_number[1]:
            count[1] = 0
        if count[2] == ck_number[2]:
            count[2] = 0
            
        if i == student_1[count[0]]:
            result[0] += 1
        if i == student_2[count[1]]:
            result[1] += 1
        if i == student_3[count[2]]:
            result[2] += 1
            
        count[0] += 1
        count[1] += 1
        count[2] += 1
        
    re_max = max(result)
    count_max = result.count(re_max)
    
    final_list = [[1,result[0]], [2,result[1]], [3,result[2]]]    
    fi_1 = sorted(final_list, key = lambda x : x[1])
    
    if count_max == 1:
        ck_1 = [fi_1[2][0]]
        return ck_1
    elif count_max == 2:
        ck_2 = [fi_1[-2][0],fi_1[-1][0]]
        ck_2.sort()
        return ck_2
    else:
        ck_3 = [fi_1[0][0],fi_1[1][0],fi_1[2][0]]
        ck_3.sort()
        return ck_3