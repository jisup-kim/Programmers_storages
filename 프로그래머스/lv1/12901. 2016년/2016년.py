def solution(a, b):
    
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [0,31,29,31,30,31,30,31,31,30,31,30]
    
    month_sum = sum(month[0:a])
    sum_month_day = month_sum + b
    total_day_divide_7 = sum_month_day % 7
    
    return day[total_day_divide_7]