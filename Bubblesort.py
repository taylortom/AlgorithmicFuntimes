#
# Bubblesort
# Time: O(n) best case, O(n2) average and worst-case 
# Space: O(1)
#
# Very simple and largely useless algorithm
# Works through the list checking pairs of elements,
# if left is bigger than right, swap.
# The biggest elements 'bubble' to the end of the list
#

import Random

# the list to sort
listToSort = Random.createRandomList(20)

# swaps the two elements in the passed list
def swap(list, index1, index2):
	index1Val = list[index1]
	index2Val = list[index2]
	list[index1] = index2Val
	list[index2] = index1Val

# sort the list
def bubblesort(list):
	while True:
		swapped = False
		
		for index in range(len(list)):
			if index == 0: continue
			
			if list[index-1] > list[index]: 
				swap(list, index-1, index)
				swapped = True
		
		if not swapped: break
			
		
		
bubblesort(listToSort)
print "SORTED GUV:", listToSort
