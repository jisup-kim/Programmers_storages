def solution(s):
    num_list = ['zero','one','two','three','four','five','six','seven','eight','nine']
    change_list = ['0','1','2','3','4','5','6','7','8','9']
    
    for dex, x in enumerate(num_list):
        if x in s:
            s = s.replace(x, change_list[dex])
    
    return int(s)
