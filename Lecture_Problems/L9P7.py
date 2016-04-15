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


class WeightedEdge(gr.Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        # Your code here
        return self.weight

    def __str__(self):
        # Your code here
        return str(self.src) + '->' + str(self.dest) + ' (' + \
               str(self.getWeight()) + ')'

node_a = gr.Node('A')
node_b = gr.Node('B')
w_edge = WeightedEdge(src=node_a, dest=node_b, weight=3)
print(w_edge)
