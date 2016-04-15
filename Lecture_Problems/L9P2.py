# coding=utf-8

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

# print('-' * 25)
# for path in sys.path:
#     print(path)


nodes = []
nodes.append(gr.Node("ABC"))  # nodes[0]
nodes.append(gr.Node("ACB"))  # nodes[1]
nodes.append(gr.Node("BAC"))  # nodes[2]
nodes.append(gr.Node("BCA"))  # nodes[3]
nodes.append(gr.Node("CAB"))  # nodes[4]
nodes.append(gr.Node("CBA"))  # nodes[5]

g = gr.Graph()
for n in nodes:
    g.addNode(n)

edges = []
edges.append(gr.Edge(nodes[0], nodes[1]))
edges.append(gr.Edge(nodes[0], nodes[2]))
edges.append(gr.Edge(nodes[1], nodes[4]))
edges.append(gr.Edge(nodes[2], nodes[3]))
edges.append(gr.Edge(nodes[3], nodes[5]))
edges.append(gr.Edge(nodes[4], nodes[5]))

for e in edges:
    g.addEdge(e)
