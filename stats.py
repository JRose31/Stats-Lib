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
	num = sorted(x)233

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


# takes the argument of quantity of numbers you want returned
def fib(x):
    try:
        #initiate list with first two numbers in sequence
        seq = [0, 1]

        while len(seq) < x:
            #add result of sum of last two numbers to initial list
            seq.append(seq[-1]+seq[-2])

        return(seq)
    except:
        print("Variable must be an integer")

#take the argument of two list, equal in dimensions and returns the Linear Regression Equation
def lin_reg(x, y):

    #Equation found @ https://www.statisticshowto.com/probability-and-statistics/regression-analysis/find-a-linear-regression-equation/

    n = len(x)

    Ex, Ey = sum(x), sum(y)

    Ex2, Ey2 = sum([i**2 for i in x]), sum([i**2 for i in y])

    Exy = sum([(num*y[idx]) for idx, num in enumerate(x)])

    '''
    print(f"Sample size: {n}")
    print(f"Sum of X: {Ex}")
    print(f"Sum of Y: {Ey}")
    print(f"Sum of X^2: {Ex2}")
    print(f"Sum of Y^2: {Ey2}")
    print(f"Sum of XY: {Exy}")
    '''

    a = round(((Ey*Ex2)-(Ex*Exy))/(n*(Ex2)-((Ex)**2)), 4)
    #print(a)

    b = round(((n*Exy)-(Ex*Ey))/((n*Ex2)-(Ex**2)), 4)
    #print(b)

    Linear_Regression = (f"y' = {a} + {b}x ")
    return(Linear_Regression)
