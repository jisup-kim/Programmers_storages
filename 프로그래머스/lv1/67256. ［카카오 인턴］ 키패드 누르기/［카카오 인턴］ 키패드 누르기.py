def solution(numbers, hand):
    distance = [[0,4,3,4,3,2,3,2,1,2],[4,0,1,2,1,2,3,2,3,4],[3,1,0,1,2,1,2,3,2,3],[4,2,1,0,3,2,1,4,3,2],[3,1,2,3,0,1,2,1,2,3],[2,2,1,2,1,0,1,2,1,2],[3,3,2,1,2,1,0,3,2,1],[2,2,3,4,1,2,3,0,1,2],[1,3,2,3,2,1,2,1,0,1],[2,4,3,2,3,2,1,2,1,0],[1,3,4,5,2,3,4,1,2,3],[1,5,4,3,4,3,2,3,2,1]]
    output = []
    left = 10
    right = 11
    
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            output.append("L")
            left = number
        elif number == 3 or number == 6 or number == 9:
            output.append("R")
            right = number
        else:
            
            if distance[left][number] > distance[right][number]:
                output.append("R")
                right = number
            elif distance[left][number] < distance[right][number]:
                output.append("L")
                left = number
            elif distance[left][number] == distance[right][number] and hand == "left":
                output.append("L")
                left = number
            else:
                output.append("R")
                right = number
    answer = ''.join(output)
    return answer