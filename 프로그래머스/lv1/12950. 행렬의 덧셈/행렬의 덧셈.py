def solution(arr1, arr2):
    
    row_leng = len(arr1)
    col_leng = len(arr1[0])
    answer = [[] * n for n in range(row_leng)]
    answer2 = answer

    for x in range(row_leng):
        for y in range(col_leng):
            answer[x].append(arr1[x][y]+arr2[x][y])
    return answer
            