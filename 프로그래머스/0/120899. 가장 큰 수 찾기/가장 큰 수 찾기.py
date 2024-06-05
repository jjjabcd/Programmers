def solution(array):
    a = max(array)
    for i, j in enumerate(array):
        if j == a:
            return [j,i]
        else:
            continue
    