# Stats-Lib
Library for statistical functions written in python. (Personal data science development project)

## Importing
```python:
from stats import *
```

## Functions
*All functions take single list only. Matrixes will not work*

### mean(x):
>Takes the mean of numbers in a list.

### median(x):
>Takes the median of numbers in a list. Averages two medians for list of even lengths.

### mode(x)
>Returns a key, value pair of key that appears the most *(the most occuring number in the list)*.

### pop_var(x):
>Takes the population variance of a set.

### samp_var(x):
>Takes the sample variance of a set. *Divides the sum of the set by n-1*

### pop_sd(x):
>Takes the square root of the population variance to get the standard deviation of the set.

### samp_sd(x):
>Takes the square root of the sample variance to get the standard deviation of the set.

### fibonacci(x):
>Takes the desired length of the returned list as an integer, returns fibonacci sequence.

### lin_reg(x, y):
>Takes the argument of two lists, equal in length, and returns the Linear Regression equation in string format
```y' = a + bx```
