# coding=utf-8

__title__ = 'test'
__version__ = '0.0.0'
__build__ = 0x000000
__author__ = 'Sam Broderick'
__license__ = 'Apache 2.0 '
__copyright__ = 'Copyright 2016 Sam Broderick'
__docformat__ = 'restructuredtext'

C = [-6, -6, -4, -4, 2, 2, 2]
C1 = [2, 2, -6, -6]
C2 = [-4, -4, 2]


def minkowskiDist(v1, v2, p):
    # type: (array, array, int) -> float
    """
    Assumes vl and v2 are equal -length arrays of numbers.
    Returns Minkowski distance of order p between vl and v2.

    :param v1: array of numbers (list).
    :type v1: array
    :param v2: array of numbers (list), equal length to v1.
    :type v2: array
    :param p: distance order
    :type p: int
    :return: Minkowski distance (p = 2 is the Euclidian distance)
    :rtype: float
    """
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i]) ** p
    return dist**(1.0/p)


def variance(cluster, mean_pos):
    # type: (list, array) -> float
    total_dist = 0.0
    for c in cluster:
        c_distance = minkowskiDist([mean_pos], [c], 2)
        total_dist += (c_distance)**2
    return total_dist

C1_mean = sum(C1)/float(len(C1))
C2_mean = sum(C2)/float(len(C2))
print('Means for C1 = {}, for C2 = {}'.format(C1_mean, C2_mean))
V1 = variance(C1, C1_mean)
print('Variance C1 = {}'.format(V1))
V2 = variance(C2, C2_mean)
print('Variance C2 = {}'.format(V2))
print('Badness = {}'.format(V1 + V2))

C1 = [2, 2, 2]
C2 = [-6, -6, -4, -4]

C1_mean = sum(C1)/float(len(C1))
C2_mean = sum(C2)/float(len(C2))
print('Means for C1 = {}, for C2 = {}'.format(C1_mean, C2_mean))
V1 = variance(C1, C1_mean)
print('Variance C1 = {}'.format(V1))
V2 = variance(C2, C2_mean)
print('Variance C2 = {}'.format(V2))
print('Badness = {}'.format(V1 + V2))
