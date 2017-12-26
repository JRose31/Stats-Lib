import math

def mean(x):
	x = sorted(x)
	return sum(x)/len(x)

def median(x):
	#determines if length of set is even or odd
	x = sorted(x)
	place = float(len(x))/float(2)

	'''if length of set is odd, dviding by two will give a x.5
	take away the .5 to get the place in the set that the median is'''
	if place.is_integer == False:
		return x[place-0.5]
	#if length is even, get average of two closest medians
	else:
		return float(x[int(place)]+x[int(place)-1])/2

def mode(x):
	x = sorted(x)
	freq = {}

	'''iterates through list and gives key value pair
	key being the instance in the list, value being 
	number of times that instance appears in the list'''
	for i in x:
		n = 0
		for e in x:
			if e == i:
				n+=1
		freq.update({i:n})

	#initial list of max key, value pair. Will update if another key shares same max value
	mx = {max(freq, key=freq.get):freq[max(freq, key=freq.get)]}

	for key, value in freq.iteritems():
		#if value of instance == value of mx, it shares the max value so add to dictionary
		if value == mx.get(mx.keys()[0]):
			mx.update({key:value})

	return mx


def pop_var(x):
	x = sorted(x)
	num = x

	#creates mean of data set
	mean = sum(num)/len(num)

	'''initializes new data set made up of the
	data points after (Xi-mean)^2 has been ran'''
	new_set = []

	#runs calculation and add it to new_set
	for i in num:
		new_set.append((i - mean)**2)

	#sum of new set divided by N(number of numbers in that set)
	variance = float(sum(new_set))/float(len(new_set))
	return variance

def samp_var(x):
	x = sorted(x)
	num = x

	#creates mean of data set
	mean = sum(num)/len(num)

	'''initializes new data set made up of the
	data points after (Xi-mean)^2 has been ran'''
	new_set = []

	#runs calculation and add it to new_set
	for i in num:
		new_set.append((i - mean)**2)

	#sum of new set divided by N(number of numbers in that set)
	variance = float(sum(new_set))/float(len(new_set)-1)
	return variance

def pop_sd(x):
	return math.sqrt(pop_var(x))

def samp_sd(x):
	return math.sqrt(samp_var(x))

