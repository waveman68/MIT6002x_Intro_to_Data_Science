import random


class intDict(object):
    """A dictionary with integer keys"""

    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey an int.  Adds an entry."""
        hashBucket = self.buckets[dictKey % self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))

    def getValue(self, dictKey):
        """Assumes dictKey an int.  Returns entry associated
           with the key dictKey"""
        hashBucket = self.buckets[dictKey % self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None

    def __str__(self):
        res = '{'
        for b in self.buckets:
            for t in b:
                res = res + str(t[0]) + ':' + str(t[1]) + ','
        return res[:-1] + '}'  # res[:-1] removes the last comma


def collision_prob(numBuckets, numInsertions):
    '''
    Given the number of buckets and the number of items to insert, 
    calculates the probability of a collision.
    '''
    prob = 1.0
    for i in range(1, numInsertions):
        prob = prob * ((numBuckets - i) / float(numBuckets))
    return 1 - prob


def sim_insertions(numBuckets, numInsertions):
    '''
    Run a simulation for numInsertions insertions into the hash table.
    '''
    choices = list(range(numBuckets))
    used = []
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used:
            return False
        else:
            used.append(hashVal)
    return True


def observe_prob(numBuckets, numInsertions, numTrials):
    '''
    Given the number of buckets and the number of items to insert, 
    runs a simulation numTrials times to observe the probability of a collision.
    '''
    probs = []
    for t in range(numTrials):
        probs.append(sim_insertions(numBuckets, numInsertions))
    return 1 - sum(probs) / float(numTrials)


def main():
    hash_table = intDict(25)
    hash_table.addEntry(15, 'a')
    #    random.seed(1) # Uncomment for consistent results
    for i in range(20):
        hash_table.addEntry(int(random.random() * (10 ** 9)), i)
    hash_table.addEntry(15, 'b')
    print(hash_table.buckets)  # evil
    print('\n', 'hash_table =', hash_table)
    print(hash_table.getValue(15))

main()

print('-------')
print('Collision probability(1000 buckets, 50 insertions) = ',
      collision_prob(1000, 50))
print('-------')
print('Collision probability(1000 buckets, 200 insertions) = ',
      collision_prob(1000, 200))
print('-------')
print('Collision prob.(1000 buckets, 50 insertions, 1000 trials = ',
      observe_prob(1000, 50, 1000))
print('-------')
print('Collision prob.(1000 buckets, 200 insertions, 1000 trials = ',
      observe_prob(1000, 200, 1000))
print('-------')
print('Collision prob.(365 buckets, 30 insertions, 1000 trials = ',
      collision_prob(365, 30))
print('-------')
print('Collision prob.(365 buckets, 250 insertions, 1000 trials = ',
      collision_prob(365, 250))

i = 31
while observe_prob(365, i, 1000) < 0.99:
    i += 1
print('Collision prob.(365 buckets, ', i, 'insertions, 1000 trials = ',
      observe_prob(365, i, 1000))
