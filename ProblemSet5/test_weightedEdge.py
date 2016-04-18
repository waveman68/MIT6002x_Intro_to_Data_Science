# coding=utf-8

from unittest import TestCase
from graph import Node, WeightedEdge
import random

__author__ = 'Sam Broderick'


class TestWeightedEdge(TestCase):
    def setUp(self):
        # set up nodes
        self.na = Node('a')
        self.nb = Node('b')
        self.nc = Node('c')

        # set up weighted edges
        self.e1 = WeightedEdge(self.na, self.nb, 15, 10)
        self.e2 = WeightedEdge(self.na, self.nc, 14, 6)
        self.e3 = WeightedEdge(self.nb, self.nc, 3, 1)

        self.print_strings = ["a->b (15, 10)", 'a->c (14, 6)', 'b->c (3, 1)']

    def test_getTotalDistance(self):
        self.assertEqual(self.e1.getTotalDistance(), 15)
        self.assertEqual(self.e2.getTotalDistance(), 14)
        self.assertEqual(self.e3.getTotalDistance(), 3)
        e_instance = random.choice([self.e1, self.e2, self.e3])
        self.assertIsInstance(e_instance.getTotalDistance(), int)

    def test_getOutdoorDistance(self):
        self.assertEqual(self.e1.getOutdoorDistance(), 10)
        self.assertEqual(self.e2.getOutdoorDistance(), 6)
        self.assertEqual(self.e3.getOutdoorDistance(), 1)
        e_instance = random.choice([self.e1, self.e2, self.e3])
        self.assertIsInstance(e_instance.getOutdoorDistance(), int)

    def test___str__(self):
        self.assertEqual(str(self.e1), self.print_strings[0])
        self.assertEqual(str(self.e2), self.print_strings[1])
        self.assertEqual(str(self.e3), self.print_strings[2])
