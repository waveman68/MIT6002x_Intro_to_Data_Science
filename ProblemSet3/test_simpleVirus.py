from unittest import TestCase
from ps3b import SimpleVirus, NoChildException

__author__ = 'Sam Broderick'


class TestSimpleVirus(TestCase):
    def setUp(self):
        global max_birth_prob, clear_prob, popDensity
        max_birth_prob = 0.97
        clear_prob = 0.05
        popDensity = 0.04
        self.test_virus1 = SimpleVirus(max_birth_prob, clear_prob)
        self.test_virus2 = SimpleVirus(1, 0)
        self.test_virus3 = SimpleVirus(0, 0)
        self.test_virus4 = SimpleVirus(0, 1)
        self.test_virus5 = SimpleVirus(1, 1)

    def test_getMaxBirthProb(self):
        global max_birth_prob
        test_max_birth_prob = self.test_virus1.getMaxBirthProb()
        self.assertIsInstance(test_max_birth_prob, float)
        self.assertLessEqual(test_max_birth_prob, 1)
        self.assertGreaterEqual(test_max_birth_prob, 0)
        self.assertTrue(test_max_birth_prob == max_birth_prob)

    def test_getClearProb(self):
        global clear_prob
        test_clear_prob = self.test_virus1.getClearProb()
        self.assertIsInstance(test_clear_prob, float)
        self.assertLessEqual(test_clear_prob, 1)
        self.assertGreaterEqual(test_clear_prob, 0)
        self.assertTrue(test_clear_prob == clear_prob)

    def test_doesClear(self):
        does_clear = self.test_virus1.doesClear()
        self.assertIsInstance(does_clear, bool)
        self.assertFalse(self.test_virus2.doesClear())
        self.assertFalse(self.test_virus3.doesClear())
        self.assertTrue(self.test_virus4.doesClear())
        self.assertTrue(self.test_virus5.doesClear())

    def test_reproduce(self):
        global popDensity
        test_reproduce = self.test_virus1.reproduce(popDensity)
        self.assertIsInstance(test_reproduce, object)
        with self.assertRaises(NoChildException):
            self.test_virus3.reproduce(popDensity)

