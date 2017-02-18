import os.path
import re
import collections
from collections import Counter

fname = "eita.txt"

if os.path.exists(fname):
    words = re.findall('\w+', open(fname).read().lower())
    counter = collections.Counter(words)
    for key,value in sorted(counter.iteritems()):
        print "Word: '{0}', frequency: '{1}'".format(key, value)

