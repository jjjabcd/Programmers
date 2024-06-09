def solution(order):
    order = str(order)
    cnt = 0
    
    for x in order:
        if x in '369':
            cnt += 1
            
    return cnt