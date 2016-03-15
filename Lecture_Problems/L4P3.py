def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    l_len = []
    for s in L:
        l_len.append(len(s))
    try:
        return stdDev(l_len)
    except ZeroDivisionError:
        return NaN


print(stdDevOfLengths([]))
