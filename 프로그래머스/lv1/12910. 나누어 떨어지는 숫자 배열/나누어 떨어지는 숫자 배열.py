def solution(arr, divisor):
    answer = []
    
    for arr_num in range(len(arr)):
        if (arr[arr_num] % divisor) == 0:
            answer.append(arr[arr_num])
    if len(answer) == 0:
        answer.append(-1)
    
    answer.sort()
    return answer