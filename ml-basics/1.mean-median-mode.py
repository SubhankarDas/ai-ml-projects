import numpy
from scipy import stats

# data set
ages = [12, 32, 13, 12, 16, 24, 25, 13, 12, 14]

# mean - average value of the data set i.e (val 1 + val 2 + ... + val n)/n
mean = numpy.mean(ages)

# median - middle most value of the set after the numbers are sorted,
# if there are two values then (val 1 + val 2)/2
median = numpy.median(ages)

# mode - most occurring element in the data set
mode = stats.mode(ages, keepdims=False)

print("mean   : ", mean)
print("median : ", median)
print("mode   : ", mode.mode, "     occurrence   : ", mode.count)
