import numpy as np
datain = np.loadtxt("data/Day13.txt",dtype=str,delimiter='\t')
instrmask = np.array([d.startswith('fold') for d in datain])

def reset():
    global dots,datain,instrmask,instructions

    dots = np.array([np.int_(d.split(',')) for d in datain[np.invert(instrmask)]])

    instructions = np.array([i[11:].split('=') for i in datain[instrmask]])
    instructions[:,0][instructions[:,0] == 'x'] = 0
    instructions[:,0][instructions[:,0] == 'y'] = 1
    instructions = instructions.astype(int)

reset()

# Part 1
print("Part 1")

instr = instructions[0]
xy = instr[0]
axis = instr[1]

mask = dots[:,xy] > axis
dots[:,xy][mask] = axis - (dots[:,xy][mask] - axis)

print("All dots: {}".format(len(dots)))
print("Unique dots: {}".format(len(np.unique(dots,axis=0))))
print("")

# Part 2
print("Part 2")

reset()
for instr in instructions:
    xy = instr[0]
    axis = instr[1]

    mask = dots[:,xy] > axis
    dots[:,xy][mask] = axis - (dots[:,xy][mask] - axis)
    dots = np.unique(dots,axis=0)

xsz = max(dots[:,0])+1
ysz = max(dots[:,1])+1
screen = np.array(['.']*xsz*ysz).reshape(ysz,xsz)
for d in dots:
    screen[tuple(d[::-1])] = '#'
im = [''.join(s) for s in screen]
for i in im:
    print(i)
