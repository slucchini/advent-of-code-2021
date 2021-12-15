import numpy as np

datain = np.loadtxt("data/Day12.txt",dtype=str)
data = np.array([s.split('-') for s in datain])

# create index
index = {}
for c in data:
    for i,ci in enumerate(c):
        if (ci in index):
            index[ci].append(c[i-1])
        else:
            index[ci] = [c[i-1]]
print(index)
print("")

# Part 1
print("Part 1")

donepaths = []
paths = []
for r in index['start']:
    paths.append(['start',r])
currentlen = len(paths[0])
while True:
    newpaths = []
    for p in paths:
        p = list(p)
        if (len(p) == currentlen):
            rooms = index[p[-1]]
            for r in rooms:
                newpaths.append(p+[r])
    currentlen += 1
    paths = newpaths
    # check for duplicate small rooms
    tokeep = np.ones(len(paths),dtype=bool)
    for i,p in enumerate(paths):
        plower = np.array([pi.lower() for pi in p])
        mask = np.where(plower == p)[0]
        smallrooms = np.array(p)[mask]
        if (len(np.unique(smallrooms)) != len(smallrooms)):
            tokeep[i] = False
    paths = np.array(paths)[tokeep]
    stillactive = np.ones(len(paths),dtype=bool)
    for i,p in enumerate(paths):
        if (p[-1] == 'end'):
            donepaths.append(p)
            stillactive[i] = False
    paths = list(paths[stillactive])
    print(len(donepaths))
    if (len(paths) == 0):
        break
print("done")
print("")

# Part 2
print("Part 2")

donepaths = []
paths = []
for r in index['start']:
    paths.append(['start',r])
currentlen = len(paths[0])
while True:
    newpaths = []
    for p in paths:
        p = list(p)
        if (len(p) == currentlen):
            rooms = index[p[-1]]
            for r in rooms:
                newpaths.append(p+[r])
    currentlen += 1
    paths = newpaths
    # check for duplicate small rooms
    tokeep = np.ones(len(paths),dtype=bool)
    for i,p in enumerate(paths):
        plower = np.array([pi.lower() for pi in p])
        mask = np.where(plower == p)[0]
        smallrooms = np.array(p)[mask]
        if (len(np.unique(smallrooms))+1 < len(smallrooms)):
            tokeep[i] = False
        elif ((len(np.where(smallrooms == 'start')[0]) > 1) | (len(np.where(smallrooms == 'end')[0]) > 1)):
            tokeep[i] = False
    paths = np.array(paths)[tokeep]
    stillactive = np.ones(len(paths),dtype=bool)
    for i,p in enumerate(paths):
        if (p[-1] == 'end'):
            donepaths.append(p)
            stillactive[i] = False
    paths = list(paths[stillactive])
    print(len(donepaths))
    if (len(paths) == 0):
        break
print("done")
