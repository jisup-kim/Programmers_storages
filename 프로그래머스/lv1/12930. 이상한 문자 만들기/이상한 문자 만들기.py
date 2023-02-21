def solution(s):
    word_list = list(s)
    index_check = 0
    
    for x in range(len(s)):
        if word_list[x] == " ":
            index_check = 0
        elif index_check == 0 or index_check % 2 == 0:
            index_check += 1
            word_list[x] = word_list[x].upper()
        else:
            index_check += 1
            word_list[x] = word_list[x].lower()
            
    return "".join(word_list)