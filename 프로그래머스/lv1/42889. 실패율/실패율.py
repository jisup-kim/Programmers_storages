def solution(N, stages):
    success_rate = [0] * (N+2)
    challenge_rate = [0] * (N+2)
    challenge_rate[0] = len(stages)
    result_list = []
    
    for where_stage in range(1,N+2):
        check_where = stages.count(where_stage)
        success_rate[where_stage] = check_where
        challenge_rate[where_stage] = challenge_rate[where_stage-1] - check_where
    challenge_rate.insert(0,0)
    challenge_rate.pop()
    print(success_rate)
    print(challenge_rate)
    
    for sr_index, success_number in enumerate(success_rate):
        if sr_index == 0 or sr_index == N+1:
            pass
        else:
            if challenge_rate[sr_index] == 0 or success_rate[sr_index] == 0:
                result_list.append([sr_index,0])
            else:
                result_list.append([sr_index,(success_rate[sr_index])/challenge_rate[sr_index]])

    result_number = sorted(result_list, key= lambda x: x[1], reverse=True)
    
    answer = []
    print(result_number)
    for i in range(len(result_number)):
        answer.append(result_number[i][0])
        
    return answer
        
    