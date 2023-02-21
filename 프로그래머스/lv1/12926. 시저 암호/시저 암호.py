
def solution(s, n):
    answer = []
    for x in range(len(s)):
        if s[x] == " ":
            answer.append(s[x])
        elif (ord(s[x]) + n) > ord("z") and (ord(s[x])) <= ord("z"):
            answer.append(chr(ord(s[x])+n-26))
        elif (ord(s[x])+n) > ord("Z") and (ord(s[x])) <= ord("Z"):
            answer.append(chr(ord(s[x])+n-26))
        else:
            answer.append(chr(ord(s[x]) + n))
    return "".join(answer)