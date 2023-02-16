def solution(seoul):
    for x in range(len(seoul)):
        if seoul[x] == "Kim":
            return "김서방은 %s에 있다" %x