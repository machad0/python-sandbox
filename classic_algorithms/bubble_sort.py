def bubbleSort(alist):
    print 'sorting:', listSort
    for i in range(len(alist) - 1):
        if alist[i] > alist[i + 1]:
            next = alist[i]
            alist[i] = alist[i+1]
            alist[i+1] = next
    return alist

listSort = [1,6,3,9,8,2,7]
for x in xrange(len(listSort) - 1):
    bubbleSort(listSort)

print 'sorted list: ', listSort
