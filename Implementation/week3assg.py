def ascending(lst):
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def alternating(l):
    if (len(l) > 1):
        if l[0] > l[1]:
            for i in range(len(l) - 1):
                if l[i] == l[i - 1]:
                    return False
            if i % 2 == 0:
                if l[i] < l[i + 1]:
                    return False
        if l[0] < l[1]:
            for i in range(len(l) - 1):
                if i % 2 == 0:
                    if l[i] > l[i + 1]:
                        return False
    return True

def matmult(X, Y):
    coln = len(Y[0])
    row = len(X)
    product = [[0 for i in range(coln)] for j in range(row)]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                product[i][j] += X[i][k] * Y[k][j]
    return product
