import pylab


# You may have to change this path
WORDLIST_FILENAME = "words.txt"

# set line width
pylab.rcParams['lines.linewidth'] = 6
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
# set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5


def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList


def make_vowel_fractions(word_list):
    vowel_fraction = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for w in word_list:
        length = float(len(w))
        num_vowels = 0
        for l in w:
            if l in vowels:
                num_vowels += 1
        vowel_fraction.append(num_vowels/length)
    return vowel_fraction


def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowel_fractions = make_vowel_fractions(wordList)
    pylab.hist(vowel_fractions, bins=numBins)
    labelPlot()
    pylab.figure()


def labelPlot():
    pylab.title('Histogram: Fraction of Vowels for Words in words.txt')
    pylab.xlabel('Vowel Fraction')
    pylab.ylabel('Frequency of Occurance')


if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
    pylab.show()
