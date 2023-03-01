def solution(n, lost, reserve):
    having_list = [1] * (n+1) # 체육복 보유 개수 리스트 초기화
    
    for x_lost in lost: # 잃어버린 사람 체크
        having_list[x_lost] -= 1
    for x_reserve in reserve: # 여분있는 사람 체크
        having_list[x_reserve] += 1
    
    for check_list in range(1,n+1): # 체육복 리스트 불러오기
        if having_list[check_list] >= 1: # 빌릴 필요 없으면 pass
            pass
        else: # having_list[check_list] == 0 [빌릴 사람]
            if check_list == 1: # 체격이 제일 작은 사람 [최소 케이스]
                if having_list[check_list+1] >= 2:
                    having_list[check_list] += 1
                    having_list[check_list+1] -= 1
            elif check_list == n: # 체격이 제일 큰 사람 [최대 케이스]
                if having_list[check_list-1] >= 2:
                    having_list[check_list] += 1
                    having_list[check_list-1] -= 1
            else: # 양 옆에 사람이 있는 경우
                if having_list[check_list-1] >= 2: # 작은 사람한테 먼저 빌리기
                    having_list[check_list] += 1
                    having_list[check_list-1] -= 1
                elif having_list[check_list+1] >= 2: # 큰 사람한테 빌리기
                    having_list[check_list] += 1
                    having_list[check_list+1] -= 1
                else:
                    print("빌려 줄 체육복이 양쪽 다 없습니다.")
    
    check_student = 0
    for i in range(1,n+1):
        if having_list[i] >= 1:
            check_student += 1

    return check_student