
def solution(s):

    check_list = []
    for i in range(len(s)):
        x = s[i]
        if len(check_list) == 0 and x == ")":
            return False
        
        elif x == "(":
            check_list.append(x)
        else:
            open_x = check_list[-1]
            if open_x == "(" and x == ")":
                check_list.pop()
                
    if len(check_list) == 0:
        return True
    else:
        return False
