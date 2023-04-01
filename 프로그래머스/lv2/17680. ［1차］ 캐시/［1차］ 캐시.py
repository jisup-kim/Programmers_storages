from collections import deque

def solution(cacheSize, cities):
    storage = deque()
    run_time = 0
    
    for city in cities:
        city = city.upper()
        if city in storage:
            run_time += 1
        else:
            run_time += 5
        
        if cacheSize == 0:
            continue
        elif len(storage) < cacheSize:
            storage.append(city)
        else:
            if city in storage:
                indexs = storage.index(city)
                del storage[indexs]
                storage.append(city)
            else:
                storage.popleft()
                storage.append(city)
        
        
    return run_time
        