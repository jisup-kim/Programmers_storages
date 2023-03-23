def solution(n,a,b):
    count = 1
    if a > b: a,b = b,a
    if a+1 == b and a%2 == 1:
        return 1
    
    while True:
        if a%2 == 1: a = a+1
        if b%2 == 1: b = b+1
        #print(a,b)
        a,b = a//2, b//2
        count += 1
        if a+1 == b and a%2==1:
            return count
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')

    #return answer