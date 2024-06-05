def solution(num, k):
    cnt = str(num).find(str(k))
    if cnt == -1:
        return cnt
    else:
        return cnt+1