# Stats-Lib
Library for statistical functions written in python. (Personal data science development project)

## Importing
*from stats import **

###Functions
*All functions take single list only. Matrixes will not work*

##mean(x):
Takes the mean of numbers in a list.

##median(x):
Takes the median of numbers in a list. Averages two medians for list of even lengths.

##mode(x)
*BUG: ONLY RETURNS ONE MODE EVEN WHEN THERE IS TWO VALUES OF THE SAME MAXIMUM FREQUENCY*

##pop_var(x):
Takes the population variance of a set.

##samp_var(x):
Takes the sample variance of a set. *Divides the sum of the set by n-1*

##pop_sd(x):
Takes the square root of the population variance to get the standard deviation of the set.

##samp_sd(x):
Takes the square root of the sample variance to get the standard deviation of the set.

