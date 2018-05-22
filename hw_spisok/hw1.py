lis = [[1, 2, [3, [4, 5]], 6, 7, [8, [9]]]]
res1 = []
res2 = []

#recur
def f1(l, _len, res):
    for i in range(0, _len):

        if type(l[i]) != list:
            res.append(l[i])
        else:
            f1(l[i], len(l[i]), res)
    return res

#algor
def f2(l, _len):
    q = 0
    i = 0
    res = []
    backInd = []
    backLen = []
    backList = []
    while q <= _len:
        if (q == _len or q > _len) and len(backInd) != 0:
            q = backInd[i - 1] + 1
            backInd.pop()
            l = backList[i - 1]
            backList.pop()
            _len = len(l)
            i -= 1
            if q == _len or q > _len:
                continue
        elif q == _len and len(backInd) == 0:
            break
        if type(l[q]) != list:
            res.append(l[q])
            q += 1
        else:
            backInd.append(q)
            backList.append(l)
            _len = len(l[q])
            l = l[q]
            q = 0
            i += 1

    return res

Rec = f1(lis, len(lis), res1)
print("Рекурсия: ", Rec)

Alg = f2(lis, len(lis))
print("Алгоритм: ", Alg)
