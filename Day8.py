import numpy as np

datain = np.loadtxt("data/Day8.txt",dtype='str')
inputs = datain[:,:10]
outputs = datain[:,11:]

allsegments = ['b','a','c','d','e','g','f']
defaultnumbers = ['012456','26','12345','12356','0236','01356','013456','126','0123456','012356']

# Part 1
print("Part 1")

outlen = np.array([len(o) for o in outputs.flatten()])
mask = (outlen == 2) | (outlen == 4) | (outlen == 3) | (outlen == 7)
print("{}".format(len(outlen[mask])))
print("")

# Part 2
print("Part 2")

def print_segment(s):
    print(" "+s[1]*4+" ")
    print(s[0]+"    "+s[2])
    print(s[0]+"    "+s[2])
    print(" "+s[3]*4+" ")
    print(s[4]+"    "+s[6])
    print(s[4]+"    "+s[6])
    print(" "+s[5]*4+" ")

def rewrite_output(output,seglabels):
    newout = []
    for o in output:
        newo = str(o)
        for j,sl in enumerate(seglabels):
            newo = newo.replace(sl,str(j))
        newout.append(''.join(sorted(newo)))
    return newout

def translate_output(output):
    global defaultnumbers
    result = []
    for o in output:
        result.append(defaultnumbers.index(o))
    return int(''.join(list(np.array(result).astype(str))))

def solve(i):

    seglabels = np.zeros(7,dtype=str)
    ilens = np.array([len(ii) for ii in i])
    orderedi = ['']*len(i)
    orderedi[1] = i[ilens == 2][0]
    orderedi[4] = i[ilens == 4][0]
    orderedi[7] = i[ilens == 3][0]
    orderedi[8] = i[ilens == 7][0]

    # determine segment 1 by looking at difference between '7' and '1'
    seg1 = orderedi[7]
    for char in orderedi[7]:
        if (char not in list(orderedi[1])):
            seglabels[1] = char

    # determine segment 2 by looking at missing pieces from '0','6','9' and comparing with '1'
    sixs = i[ilens == 6]
    missingsegs = np.zeros(len(sixs),dtype=str)
    for j,s in enumerate(sixs):
        for seg in allsegments:
            if (seg not in list(s)):
                missingsegs[j] = seg
    for seg in missingsegs:
        if (seg in list(orderedi[1])):
            seglabels[2] = seg

    # segment 1 is what's left in '1'
    if (seglabels[2] == orderedi[1][0]):
        seglabels[6] = orderedi[1][1]
    else:
        seglabels[6] = orderedi[1][0]

    # segment 0 is the segment that only occurs once in '2','3','5' and also in '4'
    fives = i[ilens == 5]
    allfives = ''.join(fives)
    fivesegs = np.unique(allfives)
    singles = []
    for seg in fivesegs[0]:
        count = len(np.where(np.array(list(allfives)) == seg)[0])
        if (count == 1):
            singles.append(seg)
    for seg in singles:
        if (seg in list(orderedi[4])):
            seglabels[0] = seg
            singles.pop(singles.index(seg))

    # segement 4 is the other segment that that only occurs once in '2','3','5'
    seglabels[4] = singles[0]

    # segment 3 is what's left in '4'
    for seg in orderedi[4]:
        if (seg not in seglabels):
            seglabels[3] = seg
            break

    # segment 5 is what's left
    for seg in allsegments:
        if (seg not in seglabels):
            seglabels[5] = seg
            break

    return seglabels

print("Segments are labelled as:")
print_segment('0123456')
print("")

s = 0
for j in range(len(inputs)):
    seglabels = solve(inputs[j])
    result = translate_output(rewrite_output(outputs[j],seglabels))
    s += result

print("Sum: {}".format(s))
