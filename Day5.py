import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data/Day5.txt",dtype=str)
starts = np.array([np.int_(d.split(',')) for d in data[:,0]])
ends = np.array([np.int_(d.split(',')) for d in data[:,2]])
gridsz = np.max(np.concatenate((starts.flatten(),ends.flatten())))
print("Grid size:",gridsz)
grid = np.zeros((gridsz+1,gridsz+1))

# Part 1

verticals = np.where(starts[:,1] == ends[:,1])[0]
horizontals = np.where(starts[:,0] == ends[:,0])[0]

grid = np.zeros((gridsz+1,gridsz+1))
for i in verticals:
    st = starts[i]
    en = ends[i]
    s = min([st[0],en[0]])
    e = max([st[0],en[0]])
    grid[s:e+1,st[1]] += 1
for i in horizontals:
    st = starts[i]
    en = ends[i]
    s = min([st[1],en[1]])
    e = max([st[1],en[1]])
    grid[st[0],s:e+1] += 1

plt.imshow(grid.T)
plt.colorbar()
plt.show()

print("Part 1")
print(len(grid[grid >= 2]))
print("")

# Part 2

diagonals = np.where(np.all(list(zip((starts[:,0] != ends[:,0]),(starts[:,1] != ends[:,1]))),axis=1))[0]

for i in diagonals:
    s = starts[i]
    e = ends[i]
    delta = [e[0]-s[0],e[1]-s[1]]
    for j in range(np.abs(delta[0])+1):
        grid[s[0]+np.sign(delta[0])*j,s[1]+np.sign(delta[1])*j] += 1

plt.imshow(grid.T)
plt.colorbar()
plt.show()

print("Part 2")
print(len(grid[grid >= 2]))
