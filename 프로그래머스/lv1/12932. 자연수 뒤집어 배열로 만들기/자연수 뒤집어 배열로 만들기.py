def solution(n):
    n_list = list(str(n))
    answer = []
    for x in range(len(n_list)):
        answer.append(int(n_list[x]))
    
    answer.reverse()
    
    return answer
        