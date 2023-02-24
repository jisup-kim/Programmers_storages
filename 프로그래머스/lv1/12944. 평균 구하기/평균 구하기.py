import math

def solution(arr):
    sum = 0
    for x in arr:
        sum += x
    answer = sum / len(arr)
    return answer