#
# Basic Quicksort
# Time: O(n log n) O(n2) worst-case
# Space: O(n)
#
# List is split into two at a pivot point half way through the list
# Items smaller than the pivot go into one list, larger items in the other
# The algorithm is called recursively on the two lists
#

import Random

# the list to sort
list = Random.createRandomList(10)
sorted = []

# sort the list
def quicksort(toSort):
	if len(toSort) <= 1: return toSort # no need to sort an empty list
	
	pivotIndex = len(toSort)/2
	pivot = toSort[pivotIndex]
	toSort.pop(pivotIndex)
	
	# partition the list
	lower = []
	higher = []
	for i in range(len(toSort)):
		item = toSort[i]
		if item <= pivot: lower.append(item)
		else: higher.append(item)
	
	return (quicksort(lower) + [pivot] + quicksort(higher))

sorted = quicksort(list)	
print 'SORTED GUV:', sorted