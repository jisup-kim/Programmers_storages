from collections import Counter

def solution(k, tangerine):
    count = 0
    coun = Counter(tangerine)
    coun = dict(coun.most_common())
    for couns in coun.values():
        k -= couns
        count += 1
        if k <= 0:
            return count