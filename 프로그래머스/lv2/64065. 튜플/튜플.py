def solution(s):
    array = []
    total_array = [[] for _ in range(1000001)]
    result = []
    new_data = ""
    
    for index,x in enumerate(s):
        if (x.isdigit() == True):
            new_data += x
            if (s[index+1].isdigit() == False):
                array.append(new_data)
                new_data = ""
                
            if s[index+1] == '}':
                length = len(array)
                total_array[length].append(array)
                array = []
    
    for index,checks in enumerate(total_array):
        if index == 0:
            continue
        if len(checks) == 0:
            break
        for check in checks[0]:
            if int(check) not in result:
                result.append(int(check))
    return result
    