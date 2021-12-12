import numpy as np

datain = np.loadtxt("data/Day11.txt",dtype=str)
data = np.array([list(r) for r in datain]).astype(int)

def reset():
    global data
    data = np.array([list(r) for r in datain]).astype(int)

# Part 1
print("Part 1")

# assumes data is square
def flash(data,index):
    index = np.array(index)
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            loc = index+[i,j]
            if (np.any(loc >= len(data)) | np.any(loc < 0)):
                continue
            data[tuple(index+[i,j])] += 1
    return data

nsteps = 100
nflashes = 0
reset()
for n in range(nsteps):
    data += 1
    flashed = []
    newcharged = True
    while True:
        charged = np.array(np.where(data > 9)).T
        if (len(charged) == 0):
            break
        if (len(flashed) == 0):
            alreadyflashed = np.zeros(len(charged),dtype=bool)
        else:
            alreadyflashed = np.array([(np.array(flashed) == np.array(c)).all(1).any() for c in charged])
        newcharged = charged[np.invert(alreadyflashed)]
        if (len(newcharged) == 0):
            break
        for index in newcharged:
            data = flash(data,index)
            nflashes += 1
            flashed.append(index)
    data[data > 9] = 0

print("{} flashes in {} steps".format(nflashes,nsteps))
print("")

# Part 2
print("Part 2")

nsteps = 1000
nflashes = 0
reset()
for n in range(nsteps):
    data += 1
    flashed = []
    newcharged = True
    while True:
        charged = np.array(np.where(data > 9)).T
        if (len(charged) == 0):
            break
        if (len(flashed) == 0):
            alreadyflashed = np.zeros(len(charged),dtype=bool)
        else:
            alreadyflashed = np.array([(np.array(flashed) == np.array(c)).all(1).any() for c in charged])
        newcharged = charged[np.invert(alreadyflashed)]
        if (len(newcharged) == 0):
            break
        for index in newcharged:
            data = flash(data,index)
            nflashes += 1
            flashed.append(index)
    data[data > 9] = 0
    if np.all(data == 0):
        print("All flash on step {}!".format(n+1))
        break
