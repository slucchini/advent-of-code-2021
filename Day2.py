import numpy as np
# data = np.loadtxt("data/Day2.txt",dtype=np.dtype([('dir', str), ('num', int)]))
data = np.loadtxt("data/Day2.txt",dtype=str)
direction = data[:,0]
distance = data[:,1].astype(int)

# Part 1
print("Part 1")
hpos = np.sum(distance[direction == 'forward'])
depth = np.sum(distance[direction == 'down']) - np.sum(distance[direction == 'up'])
print(hpos)
print(depth)
print(hpos*depth)
print("")

# Part 2
print("Part 2")
hpos = 0
aim = 0
depth = 0
for i in range(len(data)):
    d = direction[i]
    x = distance[i]
    if (d == 'down'):
        aim += x
    elif (d == 'up'):
        aim -= x
    elif (d == 'forward'):
        hpos += x
        depth += aim*x

print(hpos)
print(depth)
print(hpos*depth)
