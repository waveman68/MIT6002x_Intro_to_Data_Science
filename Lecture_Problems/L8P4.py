# coding=utf-8

from itertools import chain, combinations


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', ' \
                 + str(self.weight) + '>'
        return result


def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items


# generate all combinations of N items
def powerSet(items):
    # type: (list) -> list
    """
    Generate a powerset of the set of items
    :param items: list of items (set)
    """
    # enumerate the 2**N possible combinations
    for subset in chain.from_iterable(combinations(items, r) for r in
                                      range(len(items) + 1)):
        yield list(subset)


def yieldAllCombos(items):
    # type: (list) -> tuple
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.

    :rtype: tuple
    :param items: items to be sorted in bag1 or bag2
    """
    # Your code here
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3 ** N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i / 3**j) % 3 == 1:
                bag1.append(items[j])
            elif (i / 3**j) % 3 == 2:
                bag2.append(items[j])
            else:
                pass
        yield (bag1, bag2)


my_items = buildItems()
my_combos = yieldAllCombos(my_items)
# for i in my_combos:
#     print(i)
# print('=====')
# print(Item('clock', 175, 10))

seq = ['A', 'B', 'C', 'D', 'E']
for i in powerSet(seq):
    print(i)
