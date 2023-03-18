
def solution(s):

    check_list = []
    for i in range(len(s)):
        if len(check_list) == 0 and s[i] == ")":
            return False
        
        elif s[i] == "(":
            check_list.append(s[i])
        else:
            open_x = check_list[-1]
            if open_x == "(" and s[i] == ")":
                check_list.pop()
                
    if len(check_list) == 0:
        return True
    else:
        return False
