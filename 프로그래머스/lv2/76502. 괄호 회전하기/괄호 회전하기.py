from collections import deque

def solution(s):
    q = deque(s)
    count = 0
    for x in range(len(s)):
        if x == 0:
            pass
        else:
            quan = q.popleft()
            q.append(quan)
        check = []
        
        for index,data in enumerate(q, start=1):
            #print("들어온 데이터 : {}".format(data))
            if (data in [']',')','}']) and (len(check) == 0):
                #print("1번 루프 통과")
                break
            elif (data in ['[','(','{']):
                #print("2번 루프 통과")
                check.append(data)
            else:
                #print("3번 루프 통과")
                if (check[-1] == '(') and (data == ')') or (check[-1] == '[') and (data == ']') or (check[-1] == '{') and (data == '}'):
                    #print("3-1번 루프 통과")
                    check.pop()
                else:
                    #print("3-2번 루프 통과")
                    break
            if (len(check) == 0) and (index == len(q)):
                #print("다 돌고 텅텅 비었다")
                count += 1
    return count