from collections import deque

def solution(progresses, speeds):
    q = deque(progresses)
    q_s = deque(speeds)
    result = []
    count = 0
    
    while q:
        for x in range(len(q)):
            q[x] = q[x] + q_s[x]
        
        for y in range(len(q)):
            if q[y] >= 100:
                count += 1
            else:
                break
        if count >= 1:
            result.append(count)
            
            for _ in range(count):
                q.popleft()
                q_s.popleft()
            count = 0  
    return result
        
                