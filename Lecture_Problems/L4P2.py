def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = [3, 3, 3, 3, 3, 3, 3]
l3 = [0, 0, 0, 3, 6, 6, 6]
print('Variances are: ', stdDev(l1), stdDev(l2), stdDev(l3))

l4 = [3, 3, 5, 7, 7]
l5 = [1, 5, 5, 5, 9]
print('Variances are: ', stdDev(l4), stdDev(l5))
