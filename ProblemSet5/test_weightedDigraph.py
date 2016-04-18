from unittest import TestCase
from graph import Node, WeightedEdge, WeightedDigraph
from string import split

__author__ = 'Sam Broderick'


class TestWeightedDigraph(TestCase):
    def setUp(self):
        # set up nodes
        self.na = Node('a')
        self.nb = Node('b')
        self.nc = Node('c')

        # set up weighted edges
        self.e1 = WeightedEdge(self.na, self.nb, 15, 10)
        self.e2 = WeightedEdge(self.na, self.nc, 14, 6)
        self.e3 = WeightedEdge(self.nb, self.nc, 3, 1)

        self.g = WeightedDigraph()

        self.g.addNode(self.na)
        self.g.addNode(self.nb)
        self.g.addNode(self.nc)

        self.g.addEdge(self.e1)
        self.g.addEdge(self.e2)
        self.g.addEdge(self.e3)

        self.print_strings = ["a->b (15.0, 10.0)", 'a->c (14.0, 6.0)', 'b->c (3.0, 1.0)']

    def test_addEdge(self):
        self.assertEquals(self.g.hasNode(self.e1.getDestination()), True)
        self.assertEquals(self.g.hasNode(self.e1.getSource()), True)

        self.assertEquals(self.g.hasNode(self.e2.getDestination()), True)
        self.assertEquals(self.g.hasNode(self.e2.getSource()), True)

        self.assertEquals(self.g.hasNode(self.e3.getDestination()), True)
        self.assertEquals(self.g.hasNode(self.e3.getSource()), True)

    def test_childrenOf(self):
        for node in self.g.nodes:
            children = self.g.childrenOf(node)
            for child in children:
                self.assertIsInstance(child, Node)

    def test___str__(self):
        my_str = str(self.g)
        test_list = split(str(self.g), '\n')
        print('my_str is: {0}'.format(my_str))
        print('test_list is: {0}'.format(test_list))
        self.assertEqual(test_list[0], self.print_strings[0])
        self.assertEqual(test_list[1], self.print_strings[1])
        self.assertEqual(test_list[2], self.print_strings[2])
