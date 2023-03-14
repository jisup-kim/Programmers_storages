from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    
    def bfs(x,y):
        q.append([x,y])
        
        while q:
            x,y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx >= n or nx <= -1 or ny >= m or ny <= -1:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append([nx,ny])
    bfs(0,0)
    result = maps[n-1][m-1]
    
    if result == 1:
        return -1
    else:
        return result
    