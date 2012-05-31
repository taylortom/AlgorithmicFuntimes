#
# In-place Quicksort
# Time: O(n log n) O(n2) worst-case 
# Space: O(log n)
#
# Partition algorithm moves all elements less than a pivot point to one part of the array, 
# and all elements larger to the other part, returning the final position of the pivot in the array.
#
# Each call to the algorithm reduces the array by at least one element, since the element at pivotNewIndex 
# is placed in its final position.
#

import Random

# the list to sort
listToSort = Random.createRandomList(10)
sorted = []

# swaps the two elements in the passed list
def swap(list, index1, index2):
	index1Val = list[index1]
	index2Val = list[index2]
	list[index1] = index2Val
	list[index2] = index1Val
	
# sorts the 
def partition(list, left, right, pivotIndex):
	pivotVal = list[pivotIndex]
	swap(list, pivotIndex, right)
	storeIndex = left
	
	for index in range(left, right):
		if list[index] < pivotVal: 
			swap(list, index, storeIndex)
			storeIndex = storeIndex + 1
			
	swap(list, storeIndex, right)
	return storeIndex
			
# sort the list
def quicksort(list, left, right):
	if left < right:
		
		# get a pivot index
		pivotIndex = Random.getRandomInt(len(listToSort))
		while pivotIndex < left or pivotIndex > right: 
			pivotIndex = Random.getRandomInt(len(listToSort))
		
		pivotNewIndex = partition(list, left, right, pivotIndex)

		# Recursively sort elements on each side
		quicksort(list, left, pivotNewIndex - 1)
		quicksort(list, pivotNewIndex + 1, right)
		
quicksort(listToSort, 0, len(listToSort) - 1)
print "SORTED GUV:", listToSort
