def solution(array, commands):
    answer = []
    tem_list = []
    for command in commands:
        tem_list.append(array[command[0]-1:command[1]])
        tem_list[0].sort()
        answer.append(tem_list[0][command[2]-1])
        tem_list = []
    
    return answer