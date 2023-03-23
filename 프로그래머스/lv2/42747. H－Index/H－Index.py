def solution(citations):
    citations.sort(reverse=True)
    amount = len(citations)
    total_ea = 0

    for x in range(10000,-1,-1):
        total_ea += citations.count(x)
        
        if total_ea == x or (total_ea > x and citations.count(x)!=0):
            return x
    