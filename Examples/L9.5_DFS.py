# from graph import *

from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
import sys
import os
import importlib

my_path = '/Users/sam/PycharmProjects/MIT6002x_Intro_to_Data_Science/Examples/L9_1_graph.py'
sys.path.append(os.path.dirname(my_path))
# for path in sys.path:
#     print(path)
mname = os.path.splitext(os.path.basename(my_path))[0]
gr = importlib.import_module(mname)
sys.path.pop()


def DFS(graph, start, end, path=[], shortest=None):
    # assumes graph is a Digraph
    # assumes start and end are nodes in graph
    path = path + [start]
    print('Current dfs path:', gr.printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # avoid cycles
            newPath = DFS(graph, node, end, path, shortest)
            if newPath is not None:
                return newPath


def DFSShortest(graph, start, end, path=[], shortest=None):
    # assumes graph is a Digraph
    # assumes start and end are nodes in graph
    path = path + [start]
    print('Current dfs path:', gr.printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # avoid cycles
            if shortest is None or len(path) < len(shortest):
                newPath = DFSShortest(graph, node, end, path, shortest)
                if newPath is not None:
                    shortest = newPath
    return shortest


def testSP():
    nodes = []
    for name in range(6):
        nodes.append(gr.Node(str(name)))
    g = gr.Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(gr.Edge(nodes[0], nodes[1]))
    g.addEdge(gr.Edge(nodes[1], nodes[2]))
    g.addEdge(gr.Edge(nodes[2], nodes[3]))
    g.addEdge(gr.Edge(nodes[2], nodes[4]))
    g.addEdge(gr.Edge(nodes[3], nodes[4]))
    g.addEdge(gr.Edge(nodes[3], nodes[5]))
    g.addEdge(gr.Edge(nodes[0], nodes[2]))
    g.addEdge(gr.Edge(nodes[1], nodes[0]))
    g.addEdge(gr.Edge(nodes[3], nodes[1]))
    g.addEdge(gr.Edge(nodes[4], nodes[0]))
    sp = DFS(g, nodes[0], nodes[5])
    print('='*25)
    sp_sh = DFSShortest(g, nodes[0], nodes[5])
    print(sp)
    print('='*25)
    print('Shortest path found by DFS:', gr.printPath(sp))
    print('='*25)
    print('Shortest path found by DFSShortest:', gr.printPath(sp_sh))

testSP()
