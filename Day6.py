import numpy as np
from tqdm import tqdm_notebook as tqdm
datain = np.loadtxt("data/Day6.txt",dtype=str)
data = np.array(str(datain).split(',')).astype(int)
# data = np.array([3,4,3,1,2])

# Part 1
ndays = 80
fish = np.copy(data)
for i in range(ndays):
    fish -= 1
    newfish = len(fish[fish < 0])
    # add new fish
    fish = np.append(fish,np.ones(newfish)*8)
    # reset old fish
    fish[fish < 0] = 6

print("Part 1")
print("{} fish after {} days.".format(len(fish),ndays))
print("")

# Part 2
fisharr = np.zeros(9)
for d in data:
    fisharr[d] += 1
fisharr = np.array(fisharr)

ndays = 256
for d in range(ndays):
    pregfish = fisharr[0]
    fisharr = np.concatenate((fisharr[1:],[pregfish]))
    fisharr[6] += pregfish

print("Part 2")
print("{} fish after {} days.".format(int(np.sum(fisharr)),d+1))
