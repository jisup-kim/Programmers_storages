def solution(arr):
    ch_least = []
          
    if len(arr) == 1:
        arr.pop()
        arr.append(-1)
        return arr
    else:
        ch_least = sorted(arr)
        arr.pop(arr.index(ch_least[0]))
        return arr