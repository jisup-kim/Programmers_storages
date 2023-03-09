def solution(today, terms, privacies):
    term_name = []
    term_month = []
    result_ch = []
    
    y_now, m_now, d_now = today.split(".")
    
    for x in terms:
        x_name, x_month = x.split()
        term_name.append(x_name)
        term_month.append(x_month)
        
    for index, y in enumerate(privacies, start=1):
        pri_date, pri_period = y.split()
        y_pri, m_pri, d_pri = pri_date.split(".")
        add_month = term_month[term_name.index(pri_period)]
        sum_month = int(m_pri) + int(add_month)
        
        if int(sum_month) > 12:
            remain_month = int(sum_month) % 12
            add_year = int(sum_month) // 12
            
            if int(m_pri) == 12 and int(add_month) >= 12 and int(add_month) % 12 == 0:
                y_pri = int(y_pri) + int(add_year) - 1
                m_pri = 12
            elif sum_month > 12 and sum_month % 12 == 0:
                y_pri = int(y_pri) + int(add_year) -1
                m_pri = 12
            else:
                if remain_month == 0:
                    remain_month = 1
                y_pri = int(y_pri) + int(add_year)
                m_pri = remain_month
                
        else:
            m_pri = sum_month
        print(y_pri,m_pri,d_pri)
        if int(y_pri) < int(y_now) or (int(y_pri) == int(y_now) and int(m_pri) < int(m_now)) or (int(y_pri) == int(y_now) and int(m_pri) == int(m_now) and int(d_pri) <= int(d_now)):
            result_ch.append(index)
            
    
    return result_ch