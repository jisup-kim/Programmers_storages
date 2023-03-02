def solution(board, moves):
    count = []
    check = 0
    basket = []
    for x in moves:
        move = x-1
        for a_board in board:
            if a_board[move] == 0:
                pass
            else:                
                basket.append(a_board[move])
                a_board[move] = 0      
                break
                
    def check(baskets, counts):
        for x in range(1,len(baskets)):
            if baskets[x] == baskets[x-1]:
                del baskets[x]
                del baskets[x-1]
                counts.append(1)
                check(baskets, counts)
                break
                
    check(basket, count)  
    answer = len(count) * 2
    return answer