def solution(s):
    change = ""
    for i in range(len(s)):
        
        if i == len(s)-1:
            change += s[i]            
        elif (s[i+1].isdigit() == True or s[i+1].isalpha() == True) and s[i] == " ":
            change += "*"
        else:
            change += s[i]
    print(change)
    array = list(change.split("*"))
    print(array)
    answer = []
    for x in array:
        x = x.lower()
        star_count = x.count("*")
        x = x.replace("*", " ")
        if x[star_count].isdigit() == True:
            pass
        else:
            x = x[:star_count] + x[star_count].upper() + x[star_count+1:]
            
        answer.append(x)
        
    print(' '.join(answer))
    return ' '.join(answer)