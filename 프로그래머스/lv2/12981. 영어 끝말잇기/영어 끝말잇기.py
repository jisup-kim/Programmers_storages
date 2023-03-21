def solution(n, words):
    answer = []
    last_word_check = ""
    for index, i in enumerate(words):
        if i in answer or (index != 0 and last_word_check != i[0]):
            order = index + 1
            cycle = (order // n) + 1
            wrong = order % n
            if wrong == 0: wrong,cycle = n,cycle-1
            return [wrong, cycle]
        else:
            last_word_check = i[-1]
            answer.append(i)

    return [0,0]