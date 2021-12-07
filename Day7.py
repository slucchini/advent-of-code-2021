import numpy as np
import math

def fact(x):
    result = 0
    while (x > 0):
        result += x
        x -= 1
    return result

datain = np.loadtxt("data/Day7.txt",dtype='str')
data = np.array(str(datain).split(',')).astype(int)
# data = np.array([16,1,2,0,4,2,7,1,2,14])

# plt.hist(data,bins=50)
# plt.show()

# Part 1
print("Part 1")
fuel = 0
print("Median: {}".format(int(np.median(data))))
for d in data:
    fuel += np.abs(d - int(np.median(data)))
print("Fuel used: {}".format(fuel))
print("")

# Part 2
print("Part 2")
fuel = 0
mean = int(np.round(np.mean(data)))
print("Mean: {}".format(mean))
for d in data:
    fuel += fact(np.abs(d - mean+1))
print("Fuel used: {}".format(fuel))
