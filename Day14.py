import numpy as np

datain = np.loadtxt("data/Day14.txt",dtype=str,delimiter='\t')
template = np.array(list(datain[0]))
rules = {d[:2]:d[-1] for d in datain[1:]}

def reset():
    global polymer
    polymer = template

reset()

# Part 1
print("Part 1")

reset()
nsteps = 10
for n in range(nsteps):
    newpoly = polymer
    for i in range(len(polymer[:-1]))[::-1]:
        pair = ''.join(polymer[i:i+2])
        if (pair in rules):
            newpoly = np.insert(newpoly,i+1,rules[pair])
    polymer = newpoly

els = np.unique(polymer)
counts = {}
for e in els:
    counts[e] = len(np.where(polymer == e)[0])
print(counts)
print(max(counts.values()) - min(counts.values()))
print("")

# Part 2

def count_pairs(poly):
    allpairs = np.array([''.join(pair) for pair in np.array(list(zip(poly,poly[1:])))])
    paircount = {}
    for p in np.unique(allpairs):
        paircount[p] = len(np.where(allpairs == p)[0])
    return paircount

def get_new_poly(paircount):
    newpaircount = {}
    for p in paircount:
        newpairs = inserts[p]
        nnew = paircount[p]
        for newpair in newpairs:
            if (newpair in newpaircount):
                newpaircount[newpair] += nnew
            else:
                newpaircount[newpair] = nnew
    return newpaircount

def get_char_counts(paircount):
    counts = {c:0 for c in np.unique(list(''.join(list(paircount.keys()))))}
    for p in paircount:
        c1,c2 = p
        counts[c1] += paircount[p]
        counts[c2] += paircount[p]
    for c in counts:
        counts[c] = int(np.ceil(counts[c]/2))
    return counts

inserts = {}
for r in rules:
    c1,c2 = r
    i = rules[r]
    inserts[r] = [c1+i,i+c2]

# Part 1 Check
print("Part 1 Method 2")
paircount = count_pairs(template)

nsteps = 10
for i in range(nsteps):
    paircount = get_new_poly(paircount)

counts = get_char_counts(paircount)
print(max(counts.values()) - min(counts.values()))
print("")

# Part 2
print("Part 2")
paircount = count_pairs(template)

nsteps = 40
for i in range(nsteps):
    paircount = get_new_poly(paircount)

counts = get_char_counts(paircount)
print(max(counts.values()) - min(counts.values()))
