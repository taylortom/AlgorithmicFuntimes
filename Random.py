#
# Module with various random functions,
# such as populating lists etc.
#

import random

# create a list of random numbers bounded by max
def createRandomList(max):

	list = []
	
	while len(list) < max:
		rand = round(random.random() * max)
		while rand > max:
			rand = round(random.random() * max)
		list.append(rand)
		
	return list

# generates a random number between 0 and upperBound
def getRandomInt(upperBound):
	return int(round(random.random() * upperBound))
	