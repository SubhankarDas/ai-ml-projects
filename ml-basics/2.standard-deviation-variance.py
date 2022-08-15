import numpy
import math

ages = [12, 32, 13, 12, 16, 24, 25, 13, 12, 14]

# standard deviation - describes how spread are the values from the average i.e mean
# less the standard deviation closer the values are to the mean
# more the standard deviation more spread the values from the mean
stnddev = numpy.std(ages)

# variance - also used to describe how spread values are from mean
# variance = standard deviation ^ 2
variance = numpy.var(ages)

print("standard deviation : ", stnddev)
print("variance           : ", variance)

# calculate variance -
# 1. calculate mean: (a + b + c)/3 = mean
# 2. calculate diff.: (a - mean) = x     (b - mean) = y     (c - mean) = z
# 3. add there squares and the average: (x^2 + y^2 + z^2)/3 = variance


# standard deviation = sqrt(variance)
print("standard deviation : ", math.sqrt(variance))

# std -> omega(σ)     var -> omega^2
