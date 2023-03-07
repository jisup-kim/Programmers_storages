def solution(id_list, report, k):
    report_name_check = []
    good_check = [[] for _ in range(len(id_list))]
    bad_check = [0] * (len(id_list))
    result = [0] * (len(id_list))
    
    for x in report:
        good, bad = x.split()
        
        b_index = id_list.index(bad)
        if good in good_check[b_index]:
            pass
        else:
            good_check[b_index].append(good)
            bad_check[b_index] += 1
                    
    for index, z in enumerate(bad_check):
        if z < k:
            pass
        else:
            for a in good_check[index]:
                number_ck = id_list.index(a)
                result[number_ck] += 1
                
        
    #print(result)
    return result