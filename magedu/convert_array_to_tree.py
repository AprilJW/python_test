lst = [30, 20, 80, 40, 50, 10, 60, 70, 90]

def genetree(lst):
    if not lst:
        return
    length = len(lst)
    cur = 0
    n = 0
    while True:
        end = 2 ** n + cur
        if end > length - 1:
            break
        [print(lst[i], end=' ') for i in range(cur, end)]
        print()
        n += 1
        cur = end
    [print(lst[i], end=' ') for i in range(cur, length)]

# genetree(lst)
genetree([i for i in range(1, 30)])


