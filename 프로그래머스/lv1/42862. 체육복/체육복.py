def solution(n, lost, reserve):
    having_list = [1] * (n+1)
    print(having_list)
    
    for x_lost in lost:
        having_list[x_lost] -= 1
    for x_reserve in reserve:
        having_list[x_reserve] += 1
    print(having_list)
    
    for check_list in range(1,n+1):
        if having_list[check_list] >= 1:
            pass
        else: # having_list[check_list] == 0
            if check_list == 1:
                if having_list[check_list+1] >= 2:
                    having_list[check_list] += 1
                    having_list[check_list+1] -= 1
            elif check_list == n:
                if having_list[check_list-1] >= 2:
                    having_list[check_list] += 1
                    having_list[check_list-1] -= 1
            else:
                if having_list[check_list-1] >= 2:
                    having_list[check_list] += 1
                    having_list[check_list-1] -= 1
                elif having_list[check_list+1] >= 2:
                    having_list[check_list] += 1
                    having_list[check_list+1] -= 1
                else:
                    print("빌려 줄 체육복이 양쪽 다 없습니다.")
    print(having_list)
    
    check_student = 0
    for i in range(1,n+1):
        if having_list[i] >= 1:
            check_student += 1
    answer = check_student
    return answer