#
# Insertion sort
# Time: O(n) best case, O(n2) average and worst-case 
# Space: O(n)
#
# List is iterated through, with each item being  
#

import Random

# the list to sort
listToSort = Random.createRandomList(20)

# sort the list
def insertionsort(list):
				
		for index in range(1, len(list)):
			item = list[index]
	
			holeIndex = index-1
			
			while holeIndex >= 0 and list[holeIndex] > item:
				list[holeIndex+1] = list[holeIndex]
				holeIndex -= 1
				
			list[holeIndex+1] = item
		
print listToSort
insertionsort(listToSort)
print "SORTED GUV:", listToSort
