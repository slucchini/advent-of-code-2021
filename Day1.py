import numpy as np
data = np.loadtxt('Day1.txt')

# Part 1
print("Part 1")
print(data)
print(np.roll(data,1))
inc = data > np.roll(data,1)
print(inc)
print(np.sum(inc))
print("")

# Part 2
print("Part 2")
sums = np.array([np.sum(data[i:i+3]) for i in range(len(data))])
inc = sums > np.roll(sums,1)
print(sums)
print(inc)
print(np.sum(inc))
