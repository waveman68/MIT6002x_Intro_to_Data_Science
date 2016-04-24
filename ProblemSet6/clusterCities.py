# Code shared across examples
from __future__ import print_function
import pylab
import string


def stdDev(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return (tot / len(X)) ** 0.5


def scaleFeatures(vals):
    """Assumes vals is a sequence of numbers"""
    result = pylab.array(vals)
    mean = sum(result) / float(len(result))
    result -= mean
    sd = stdDev(result)
    result /= sd
    return result


class Point(object):
    def __init__(self, name, originalAttrs):
        """originalAttrs is an array"""
        self.name = name
        self.attrs = originalAttrs

    def dimensionality(self):
        return len(self.attrs)

    def getAttrs(self):
        return self.attrs

    def distance(self, other):
        # Euclidean distance metric
        result = 0.0
        for i in range(self.dimensionality()):
            result += (self.attrs[i] - other.attrs[i]) ** 2
        return result ** 0.5

    def getName(self):
        return self.name

    def toStr(self):
        return self.name + str(self.attrs)

    def __str__(self):
        return self.name


class Cluster(object):
    """ A Cluster is defines as a set of elements, all having
    a particular type """

    def __init__(self, points, pointType):
        # type: (list, str) -> None
        """
        Elements of a cluster are saved in self.points and the pointType is also saved.

        :param points: list of point objects
        :type points: list
        :param pointType: no clue, but links between clusters...
        :type pointType: str
        """
        self.points = points
        self.pointType = pointType

    def singleLinkageDist(self, other):
        # type: (Cluster) -> float
        """
        Returns the float distance between the points that are closest to
        each other, where one point is from self and the other point is from
        other. Uses the Euclidean dist between 2 points, defined in Point.

        :param other: other cluster object
        :type other: Cluster
        :rtype: float
        """
        # TODO
        min_distance = None
        for point in self.points:
            for other_point in other.points:
                current_distance = point.distance(other_point)
                if min_distance is None:
                    min_distance = current_distance
                elif current_distance < min_distance:
                    min_distance = current_distance
        return min_distance

    def maxLinkageDist(self, other):
        # type: (Cluster) -> float
        """
        Returns the float distance between the points that are farthest from
        each other, where one point is from self and the other point is from
        other. Uses the Euclidean dist between 2 points, defined in Point.

        :param other: other cluster object
        :type other: Cluster
        :rtype: float
        """
        # TODO
        max_distance = None
        for point in self.points:
            for other_point in other.points:
                current_distance = point.distance(other_point)
                if max_distance is None:
                    max_distance = current_distance
                elif current_distance > max_distance:
                    max_distance = current_distance
        return max_distance

    def averageLinkageDist(self, other):
        # type: (Cluster) -> float
        """
        Returns the float average (mean) distance between all pairs of
        points, where one point is from self and the other point is from
        other. Uses the Euclidean dist between 2 points, defined in Point.

        :param other: other cluster object
        :type other: Cluster
        :rtype: float
        """
        # TODO
        avg_distance = 0
        for point in self.points:
            for other_point in other.points:
                avg_distance += point.distance(other_point)
        avg_distance /= float(len(self.points)*len(other.points))
        return avg_distance

    def members(self):
        """
        Generator to yield cluster point by point
        """
        for p in self.points:
            yield p

    def isIn(self, name):
        # type: (str) -> bool
        """
        Returns True is the element named name is in the cluster
        and False otherwise

        :param name: element name
        :type name: str
        :return: returns bool whether isIn or not
        :rtype: bool
        """
        for p in self.points:
            if p.getName() == name:
                return True
        return False

    def toStr(self):
        """Why not just use __str__ method, as it is the same?"""
        result = ''
        for p in self.points:
            result = result + p.toStr() + ', '
        return result[:-2]

    def getNames(self):
        """ For consistency, returns a sorted list of all 
        elements in the cluster """
        names = []
        for p in self.points:
            names.append(p.getName())
        return sorted(names)

    def __str__(self):
        names = self.getNames()
        result = ''
        for p in names:
            result = result + p + ', '
        return result[:-2]


class ClusterSet(object):
    """ A ClusterSet is defined as a list of clusters """

    def __init__(self, pointType):
        """
        Initialize an empty set, without any clusters

        :param pointType: Type of point
        :type pointType: str
        """
        self.members = []
        self.pointType = pointType

    def add(self, c):
        """
        Append a cluster to the end of the cluster list only if it doesn't
        already exist. If it is already in the cluster set, raise a
        ValueError.

        :param c: A cluster to be added.
        :type c: Cluster
        """
        if c in self.members:
            raise ValueError
        self.members.append(c)

    def getClusters(self):
        return self.members[:]

    def mergeClusters(self, c1, c2):
        # TODO
        """
        Assumes clusters c1 and c2 are in self.
        Adds to self a cluster containing the union of c1 and c2 and removes
        c1 and c2 from self.

        :param c1: 1st cluster
        :type c1: Cluster
        :param c2: 2nd cluster
        :type c2: Cluster
        """
        assert c1 in self.members
        assert c2 in self.members

        points = []
        for point in c1.members():
            points.append(point)

        for point in c2.members():
            points.append(point)

        merged_c = Cluster(points, self.pointType)
        self.add(merged_c)
        self.members.pop(c1)
        self.members.pop(c2)

    def findClosest(self, linkage):
        # TODO
        """
        Returns a tuple containing the two most similar clusters in self.
        Closest defined using the metric linkage.

        :param linkage: the linkage method to determine closest clusters.
        :type linkage: method
        :rtype: tuple
        """

        closest = (None, None)
        shortest = None
        for cluster1 in self.members:
            for cluster2 in self.members:
                if cluster1 == cluster2:
                    pass
                else:
                    distance = linkage(cluster1, cluster2)
                    if shortest is None or distance < shortest:
                        shortest = distance
                        closest = (cluster1, cluster2)

        return closest

    def mergeOne(self, linkage):
        # type: (method) -> tuple
        # TODO
        """
        Merges the two most simililar clusters in self
        Similar defined using the metric linkage
        Returns the clusters that were merged

        :param linkage: the linkage method to determine closest clusters.
        :type linkage: method
        :rtype: Cluster
        """
        c1, c2 = self.findClosest(linkage=linkage)
        self.mergeClusters(c1, c2)
        return c1, c2

    def numClusters(self):
        return len(self.members)

    def toStr(self):
        cNames = []
        for c in self.members:
            cNames.append(c.getNames())
        cNames.sort()
        result = ''
        for i in range(len(cNames)):
            names = ''
            for n in cNames[i]:
                names += n + ', '
            names = names[:-2]
            result += '  C' + str(i) + ':' + names + '\n'
        return result


# City climate example
class City(Point):
    pass


def readCityData(fName, scale=False):
    """Assumes scale is a Boolean.  If True, features are scaled"""
    dataFile = open(fName, 'r')
    numFeatures = 0
    # Process lines at top of file
    for line in dataFile:  # Find number of features
        if line[0:4] == '#end':  # indicates end of features
            break
        numFeatures += 1
    numFeatures -= 1
    featureVals = []

    # Produce featureVals, cityNames
    featureVals, cityNames = [], []
    for i in range(numFeatures):
        featureVals.append([])

    # Continue processing lines in file, starting after comments
    for line in dataFile:
        dataLine = string.split(line[:-1], ',')  # remove newline; then split
        cityNames.append(dataLine[0])
        for i in range(numFeatures):
            featureVals[i].append(float(dataLine[i + 1]))

    # Use featureVals to build list containing the feature vectors
    # For each city scale features, if needed
    if scale:
        for i in range(numFeatures):
            featureVals[i] = scaleFeatures(featureVals[i])
    featureVectorList = []
    for city in range(len(cityNames)):
        featureVector = []
        for feature in range(numFeatures):
            featureVector.append(featureVals[feature][city])
        featureVectorList.append(featureVector)
    return cityNames, featureVectorList


def buildCityPoints(fName, scaling):
    cityNames, featureList = readCityData(fName, scaling)
    points = []
    for i in range(len(cityNames)):
        point = City(cityNames[i], pylab.array(featureList[i]))
        points.append(point)
    return points


# Use hierarchical clustering for cities
def hCluster(points, linkage, numClusters, printHistory):
    cS = ClusterSet(City)
    for p in points:
        cS.add(Cluster([p], City))
    history = []
    while cS.numClusters() > numClusters:
        merged = cS.mergeOne(linkage)
        history.append(merged)
    if printHistory:
        print('')
        for i in range(len(history)):
            names1 = []
            for p in history[i][0].members():
                names1.append(p.getName())
            names2 = []
            for p in history[i][1].members():
                names2.append(p.getName())
            print('Step', i, 'Merged', names1, 'with', names2)
            print('')
    print('Final set of clusters:')
    print(cS.toStr())
    return cS


def test():
    points = buildCityPoints('cityTemps.txt', False)
    hCluster(points, Cluster.singleLinkageDist, 10, True)
    # points = buildCityPoints('cityTemps.txt', True)
    # hCluster(points, Cluster.maxLinkageDist, 10, False)
    # hCluster(points, Cluster.averageLinkageDist, 10, False)
    # hCluster(points, Cluster.singleLinkageDist, 10, False)

test()
