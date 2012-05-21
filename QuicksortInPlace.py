#
# This version reduces the required storage space from 
# O(n) to O(log n)
#

import random

# size of list
max = 10

# the list to sort
listToSort = []
sorted = []

# create a list of random numbers bounded by max
while len(listToSort) < max:
	rand = round(random.random() * 100)
	while rand > max:
		rand = round(random.random() * 100)
	listToSort.append(rand)

def swap(list, index1, index2):
	index1Value = list[index1]
	list[index1] = list[index2]
	list[index2] = index1Value

def partition(list, left, right, pivotIndex):
	pivot = list[pivotIndex]
	swap(list, pivotIndex, right)
	storeIndex = left
	
	for i in range(len(list)):
		if list[i] < pivot:
			swap(list, i, storeIndex)
			storeIndex = storeIndex+1
	swap(list, storeIndex, right)
	return storeIndex

def quicksort(toSort, left, right):
	if left < right:
		pivotIndex = (left+right)/2
		pivotNewIndex = partition(toSort, left, right, pivotIndex)
		quicksort(toSort, left, pivotNewIndex-1)
		quicksort(toSort, pivotNewIndex+1, right)

sorted = quicksort(listToSort, 0, max-1)
print 'sorted list:', sorted