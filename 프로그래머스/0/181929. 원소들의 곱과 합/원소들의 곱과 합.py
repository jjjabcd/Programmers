def solution(num_list):
    a = sum(num_list)**2
    dot = 1
    
    for i in (num_list):
        dot = dot * i
        
    if a > dot:
        return 1
    else:
        return 0