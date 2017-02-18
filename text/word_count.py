##Count Words in a String Counts the number of individual words in a string.
##For added complexity read these strings in from a text file and generate a summary

import os.path, re, glob, collections
from collections import Counter

for file in os.listdir("/"):
    for file in glob.glob("*.txt"):
        words = re.findall('\w+', open(file).read().lower())
        counter = collections.Counter(words)
        for word, frequency in sorted(counter.iteritems()):
             print "Word: '{0}', frequency: '{1}'".format(word, frequency)
