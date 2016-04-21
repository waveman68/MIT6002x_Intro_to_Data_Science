# coding=utf-8

# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#


from __future__ import print_function
# import pprint
import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import *

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

"""
Model the buildings as nodes and the distances as edges.
Read each line from the file.
Check if the src and dest buildings exist, create nodes if not.
Save an edge with the 4 parameters.
"""


# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#


def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result += str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result


def load_map(mapFilename):
    # type: (str) -> WeightedDigraph
    """
    Parses the map file and constructs a directed graph

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    :param mapFilename: name of the file
    :type mapFilename: str
    :return: a directed graph representing the map
    :rtype: WeightedDigraph
    """
    # TODO Problem 2-1 to 2-3: Done
    print("Loading map from file...")
    g = WeightedDigraph()

    with open(name=mapFilename, buffering=0) as inFile:
        for line in inFile:
            line_list = string.split(line)

            assert len(line_list) == 4  # ensure 4 entries per line
            try:
                g.addNode(Node(line_list[0]))
            except ValueError:
                pass

            try:
                g.addNode(Node(line_list[1]))
            except ValueError:
                pass

            n_src = g.hasNode(line_list[0])
            n_dest = g.hasNode(line_list[1])

            # create one edge per line
            line_edge = WeightedEdge(src=n_src,
                                     dest=n_dest,
                                     weight1=int(line_list[2]),
                                     weight2=int(line_list[3]))
            g.addEdge(line_edge)
    return g


#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#
"""
Traverse graph to find all graphs going from start to end.
Reduce this set down to those within maxTotalDist
Reduce again down to those within maxDistOutdoors
"""


# class PathDist_property(object):
#     # Class takes a path in a digraph and calculates distances
#
#     def __init__(self, path, a_digraph):
#         self.path = path
#         self.digraph = a_digraph
#
#     @property
#     def dist(self):
#         distance = 0
#
#         for i in range(len(self.path) - 1):
#             node_edges = self.digraph.getEdges(self.path[i])
#             next_node = self.path[i + 1]
#             for an_edge in node_edges:
#                 if an_edge[0] == next_node:
#                     distance += an_edge[1][0]
#         return distance
#
#     @property
#     def dist_outdoor(self):
#         distance = 0
#
#         for i in range(len(self.path) - 1):
#             node_edges = self.digraph.getEdges(self.path[i])
#             next_node = self.path[i + 1]
#             for an_edge in node_edges:
#                 if an_edge[0] == next_node:
#                     distance += an_edge[1][1]
#         return distance


def DFS_all(graph, start, end, path=[], memo=dict()):
    # type: (WeightedDigraph, str, str, list, dict) -> list
    """
    Assumes graph is a Digraph
    Assumes start and end are nodes in graph.

    :param graph: instance of class Digraph or its subclass
    :type graph: WeightedDigraph
    :param start: start building numbers (string)
    :type start: str
    :param end: end building numbers (string)
    :type end: str
    :param path: list of nodes in the path
    :type path: list
    :param memo: memoization of the paths
    :type memo: dict
    :return: None
    """
    if type(start) == str:
        start = graph.hasNode(start)
    if type(end) == str:
        end = graph.hasNode(end)
    path = path + [str(start)]
    # if path[-1] == end:
    #     print('Current dfs path:', printPath(path))
    if start == end:
        return path
    for e in graph.getEdges(start):
        if str(e[0]) not in path:  # avoid cycles
            newPath = DFS_all(graph, e[0], end, path, memo)
            key = ''.join(newPath)  # path as a string
            if newPath[-1] == str(end) and key not in memo:
                memo[key] = newPath  # value = path
    return path


def get_dist(graph, path):
    # type: (WeightedDigraph, list) -> int
    path_dist = 0
    for i in range(len(path) - 1):  # iterate over nodes
        first = graph.hasNode(path[i])
        second = graph.hasNode(path[i + 1])
        path_dist += graph.dist(first, second)
    return path_dist


def get_outdoor_dist(graph, path):
    # type: (WeightedDigraph, list) -> int
    outdoor_dist = 0
    for i in range(len(path) - 1):  # iterate over nodes
        first = graph.hasNode(path[i])
        second = graph.hasNode(path[i + 1])
        outdoor_dist += graph.dist_outdoor(first, second)
    return outdoor_dist


def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    # type: (WeightedDigraph, str, str, int, int) -> list
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.

    :param digraph: instance of class Digraph or its subclass
    :type digraph: WeightedDigraph
    :param start: start building numbers (string)
    :type start: str
    :param end: end building numbers (string)
    :type end: str
    :param maxTotalDist: maximum total distance on a path (integer)
    :type maxTotalDist: int
    :param maxDistOutdoors: maximum distance spent outdoors on a path (integer)
    :type maxDistOutdoors: int
    :rtype: list
    """

    # TODO Problem 3: DONE
    path_memo = dict()
    _ = DFS_all(
        graph=digraph,
        start=start,
        end=end,
        memo=path_memo
    )  # path not of interest, send it to _

    shortest_dist = maxTotalDist + 1  # initialize
    shortest_path = None

    for key in iter(path_memo):
        dist = get_dist(digraph, path_memo[key])
        dist_outdoor = get_outdoor_dist(digraph, path_memo[key])
        constraints = (dist <= maxTotalDist and
                       dist_outdoor <= maxDistOutdoors)
        if constraints and dist < shortest_dist:
            shortest_path = path_memo[key]
            shortest_dist = dist

    if shortest_path is None:
        raise ValueError('There is no path meeting the conditions')
    return shortest_path


#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#


def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    # type: (WeightedDigraph, str, str, int, int) -> list

    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
    not exceed maxDistOutdoors.

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.

    :param digraph: instance of class Digraph or its subclass
    :type digraph: WeightedDigraph
    :param start: start building numbers (string)
    :type start: str
    :param end: end building numbers (string)
    :type end: str
    :param maxTotalDist: maximum total distance on a path (integer)
    :type maxTotalDist: int
    :param maxDistOutdoors: maximum distance spent outdoors on a path (integer)
    :type maxDistOutdoors: int
    :rtype: list
    """

    # TODO Problem 4:
    # this is a wrapper to be compatible with the grader
    # it hides the details form the rest of the module

    def DFS_shortest(graph, start, end, maxTotalDist, maxDistOutdoors,
                     path=[], shortest_path=[], shortest_dist=1000):
        # type: (WeightedDigraph, str, str, int, int, list, list, int) -> list
        """
        Assumes graph is a Digraph
        Assumes start and end are nodes in graph.

        :param graph: instance of class Digraph or its subclass
        :type graph: WeightedDigraph
        :param start: start building numbers (string)
        :type start: str
        :param end: end building numbers (string)
        :type end: str
        :param maxTotalDist: maximum total distance on a path (integer)
        :type maxTotalDist: int
        :param maxDistOutdoors: maximum distance spent outdoors on a path (integer)
        :type maxDistOutdoors: int
        :param path: list of str nodes in the path
        :type path: list
        :param shortest_path: list of str nodes, shortest of the paths
        :type shortest_path: list
        :param shortest_dist: distance of shortest path so far
        :return: None
        """
        if type(start) == str:
            start = graph.hasNode(start)
        if type(end) == str:
            end = graph.hasNode(end)
        path = path + [str(start)]
        # if path[-1] == end:
        #     print('Current dfs path:', printPath(path))
        if start == end:
            return path
        for e in graph.getEdges(start):
            if str(e[0]) not in path:  # avoid cycles
                test_path = path + [str(e[0])]
                dist = get_dist(graph, test_path)
                dist_outdoor = get_outdoor_dist(graph, test_path)
                constraints = (dist <= maxTotalDist and
                               dist_outdoor <= maxDistOutdoors)
                if constraints and (shortest_dist is None or
                                            dist < shortest_dist):
                    newPath = DFS_shortest(graph, e[0], end, maxTotalDist,
                                           maxDistOutdoors,
                                           path=path,
                                           shortest_path=shortest_path,
                                           shortest_dist=shortest_dist)
                    if newPath is not None:
                        shortest_path = newPath
                        if len(newPath) > 0 and newPath[-1] == str(end):
                            shortest_dist = get_dist(graph, shortest_path)

        return shortest_path

    result_path = DFS_shortest(graph=digraph, start=start, end=end,
                               maxTotalDist=maxTotalDist,
                               maxDistOutdoors=maxDistOutdoors,
                               path=[], shortest_path=[],
                               shortest_dist=maxTotalDist + 1)
    if result_path is None or len(result_path) == 0:
        raise ValueError('There is no path meeting the conditions')
    return result_path


# ### NOTE! These tests may take a few minutes to run!! ####
# Uncomment below when ready to test
if __name__ == '__main__':
    # Test cases
    mitMap = load_map("mit_map.txt")
    print(isinstance(mitMap, Digraph))
    print(isinstance(mitMap, WeightedDigraph))
    # print(mitMap)
    stripped_nodes = set([int(s.getName()) for s in mitMap.nodes])  # strip out ' marks
    stripped_edges = dict()
    for k, v in mitMap.edges.items():
        stripped_edge_list = []
        for edge in v:  # value is list of edges
            stripped_edge_list.append([int(edge[0].getName()), edge[1]])
    # print('nodes', stripped_nodes)
    print('edges', stripped_edges)
    # node_1 = [s for s in mitMap.nodes_of_graph if s.getName() == '1'][0]
    # node_3 = [s for s in mitMap.nodes_of_graph if s.getName() == '3'][0]
    print('Distance 1->3 = ', mitMap.dist(mitMap.hasNode('1'),
                                          mitMap.hasNode('3')))
    print('Outdoor Distance 1->3 = ',
          mitMap.dist_outdoor(mitMap.hasNode('1'), mitMap.hasNode('3')))
    print('=' * 25)
    # pp = pprint.PrettyPrinter(depth=6)
    LARGE_DIST = 1000000
    my_dict = dict()
    # my_DFS = DFS_all(graph=mitMap, start=mitMap.hasNode('1'),
    #                  end=mitMap.hasNode('32'), memo=my_dict)
    # print(paths)

    # print('=' * 25)
    # test_path = PathDist(path=['32', '66', '56'], a_digraph=mitMap)
    # print('({}, {})'.format(test_path.dist, test_path.dist_outdoor))

    brute_force = False  # switch for long-running bruteForceSearch

    # Test case 1
    print("-" * 25)
    print("Test case 1:")
    print("Find the shortest-path from Building 32 to 56")
    expectedPath1 = ['32', '56']
    brutePath1 = (bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
                  if brute_force else expectedPath1)
    print("Expected: ", expectedPath1)
    print("Brute-force: ", brutePath1)
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print("DFS: ", dfsPath1)
    print("Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1))

    # Test case 2
    print("-" * 25)
    print("Test case 2:")
    print("Find the shortest-path from Building 32 to 56 without going outdoors")
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = (bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
                  if brute_force else expectedPath2)
    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    print("Expected: ", expectedPath2)
    print("Brute-force: ", brutePath2)
    print("DFS: ", dfsPath2)
    print("Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2))

    # Test case 3
    print("-" * 25)
    print("Test case 3:")
    print("Find the shortest-path from Building 2 to 9")
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = (bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
                  if brute_force else expectedPath3)
    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    print("Expected: ", expectedPath3)
    print("Brute-force: ", brutePath3)
    print("DFS: ", dfsPath3)
    print("Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3))

    # Test case 4
    print("-" * 25)
    print("Test case 4:")
    print("Find the shortest-path from Building 2 to 9 without going outdoors")
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = (bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
                  if brute_force else expectedPath4)
    dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
    print("Expected: ", expectedPath4)
    print("Brute-force: ", brutePath4)
    print("DFS: ", dfsPath4)
    print("Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4))

    # Test case 5
    print("-" * 25)
    print("Test case 5:")
    print("Find the shortest-path from Building 1 to 32")
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    print("Expected: ", expectedPath5)
    print("Brute-force: ", brutePath5)
    print("DFS: ", dfsPath5)
    print("Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5))

    # Test case 6
    print("-" * 25)
    print("Test case 6:")
    print("Find the shortest-path from Building 1 to 32 without going outdoors")
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = (bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
                  if brute_force else expectedPath6)
    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    print("Expected: ", expectedPath6)
    print("Brute-force: ", brutePath6)
    print("DFS: ", dfsPath6)
    print("Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6))

    # Test case 7
    print("-" * 25)
    print("Test case 7:")
    print("Find the shortest-path from Building 8 to 50 without going outdoors")
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        if brute_force:
            bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
        else:
            raise ValueError
    except ValueError:
        bruteRaisedErr = 'Yes'

    try:
        directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        dfsRaisedErr = 'Yes'

    print("Expected: No such path! Should throw a value error.")
    print("Did brute force search raise an error?", bruteRaisedErr)
    #     print("Did DFS search raise an error?", dfsRaisedErr)

    # Test case 8
    print("-" * 25)
    print("Test case 8:")
    print("Find the shortest-path from Building 10 to 32 without walking")
    print("more than 100 meters in total")
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        if brute_force:
            bruteForceSearch(mitMap, '10', '32', LARGE_DIST, 0)
        else:
            raise ValueError
    except ValueError:
        bruteRaisedErr = 'Yes'

    try:
        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'

    print("Expected: No such path! Should throw a value error.")
    print("Did brute force search raise an error?", bruteRaisedErr)
    print("Did DFS search raise an error?", dfsRaisedErr)
