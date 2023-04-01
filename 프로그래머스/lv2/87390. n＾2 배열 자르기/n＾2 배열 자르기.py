def solution(n, left, right):
    result = []
    
    start_row = left//n
    end_row = right//n
    
    start_col = left % n
    end_col = right % n
    
    
    for x in range(right-left+1):
        insert_val = start_row + 1
        #print("{}번째 시작".format(x+1))
        #print("시작 : {}번째 줄 {}번째 열".format(start_row,start_col))
        if start_row >= start_col:
            result.append(insert_val)
            #print("1. 넣은 값 : {}".format(insert_val))
            if start_col == n-1:
                start_col = 0
                start_row += 1
            else:
                start_col += 1
        else:
            insert_val = n - (n-start_col-1)
            result.append(insert_val)
            #print("2. 넣은 값 : {}".format(insert_val))
            if start_col == n-1:
                #print("끝까지 옴")
                start_col = 0
                start_row += 1
            else:
                start_col += 1
        
    return result