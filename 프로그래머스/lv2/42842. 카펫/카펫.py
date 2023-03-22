def solution(brown, yellow):

    for y in range(1,yellow+1):
        if yellow % y != 0:
            continue
        x = yellow // y
        brown_x,brown_y = x+2,y+2
        if brown_x * brown_y == brown + yellow:
            if brown_x < brown_y: brown_x,brown_y = brown_y,brown_x
            return [brown_x,brown_y]
        
    #return answer