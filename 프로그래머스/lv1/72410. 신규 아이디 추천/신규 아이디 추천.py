def solution(new_id):
    id_list = []
    
    if len(new_id) != 0:
        new_id = new_id.lower()
        
        for index, x in enumerate(new_id):
            if x.islower() == True or x.isdigit() == True or x in ("-","_","."):
                
                if index == 0 or len(id_list) == 0:
                    id_list.append(x)
                else:                   
                    if id_list[-1] == "." and x == ".":
                        pass
                    else:
                        id_list.append(x)
                        
    if len(id_list) == 0:
        pass
    elif id_list[0] == ".":
        del id_list[0]
    elif id_list[-1] == ".":
        del id_list[-1]
    else:
        pass
    
    if len(id_list) == 0:
        id_list.append("a")
    if len(id_list) >= 16:
        id_list = id_list[:15]
    if id_list[-1] == ".":
        del id_list[-1]
    if len(id_list) <= 2:
        for _ in range(2):
            if len(id_list) >= 3:
                break
            else:
                id_list.append(id_list[-1])
    
    result = "".join(id_list)
    print(result)
    return result
    
    