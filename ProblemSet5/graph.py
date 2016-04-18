# coding=utf-8

# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#


class Node(object):
    def __init__(self, name):
        self.name = str(name)

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)


class Digraph(object):
    """
    A directed graph
    """

    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]


class WeightedDigraph(Digraph):
    def __init__(self):
        super(WeightedDigraph, self).__init__()

    def addEdge(self, edge):
        # type: (WeightedEdge) -> None
        """
        Adds a weighted edge object to the weighted directional graph
        :type edge: WeightedEdge
        :param edge: a weighted edge
        """
        try:
            assert type(edge) == WeightedEdge
        except AssertionError:
            raise AssertionError('Edge is not a weighted edge. {0} not added'.
                                 format(str(edge)))
        src = edge.getSource()
        dest = edge.getDestination()
        weights = (edge.getTotalDistance(), edge.getOutdoorDistance())

        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest, weights])

    def childrenOf(self, node):
        children = self.edges[node]  # list of children incl. weights
        result = []  # initialize
        for child in children:
            result.append(child[0])  # pick node without weights
        return result

    def __str__(self):
        result = ''
        for k in self.edges:
            if len(self.edges[k]) > 0:
                for d in self.edges[k]:
                    result = '{0}{1}->{2} ({3}, {4})\n'.format(result, k, d[0],
                                                               float(d[1][0]),
                                                               float(d[1][1]))
        return result[:-1]  # without trailing \n


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight1, weight2):
        # type: (Node, Node, int, int) -> WeightedEdge
        super(WeightedEdge, self).__init__(src, dest)
        assert type(weight1) == int
        assert type(weight2) == int
        self.weight1 = weight1
        self.weight2 = weight2

    def getTotalDistance(self):
        return self.weight1

    def getOutdoorDistance(self):
        return self.weight2

    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.weight1,
                                            self.weight2)
