# -x- coding: utf-8 -x-
import random

randomList = random.sample(xrange(1, 101), 10)

def mergeSort(randomList):

    print "Split it: ", randomList

    if len(randomList) > 1:
        mid = len(randomList) / 2
        left = randomList[:mid]
        right = randomList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                randomList[k] = left[i]
                i = i + 1
            else:
                randomList[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            randomList[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            randomList[k] = right[j]
            j = j + 1
            k = k + 1

    print "Then merge it: ", randomList

mergeSort(randomList)
print "Sorted list: ", randomList
