def solution(s):
    if len(s) == 4 or len(s) == 6:
        for x in range(len(s)):
            if ord(s[x]) < 48 or ord(s[x]) > 57:
                return False  
    else:
        return False
    
    return True