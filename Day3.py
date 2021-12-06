import numpy as np
data = np.loadtxt("data/Day3.txt",dtype=str)
datarr = np.array([list(d) for d in data]).astype(int)

print("Part 1")
gamma = ''
epsilon = ''
for r in range(len(datarr[0])):
    m = np.mean(datarr[:,r])
    if (m > 0.5):
        gamma += '1'
        epsilon += '0'
    elif (m < 0.5):
        gamma += '0'
        epsilon += '1'
    else:
        print("Error")

print(gamma,'=',int(gamma,2))
print(epsilon,'=',int(epsilon,2))
print(int(gamma,2)*int(epsilon,2))
print("")

print("Part 2")
O2mask = np.ones(len(datarr),dtype=bool)
O2val = 0
O2done = False
CO2mask = np.ones(len(datarr),dtype=bool)
CO2val = 0
CO2done = False

for r in range(len(datarr[0])):
    O2m = np.mean(datarr[O2mask][:,r])
    CO2m = np.mean(datarr[CO2mask][:,r])
    if (O2m >= 0.5):
        O2val = 1
    else:
        O2val = 0
    if (CO2m >= 0.5):
        CO2val = 0
    else:
        CO2val = 1

    if (not O2done):
        O2mask = O2mask & (datarr[:,r] == O2val)
    if (not CO2done):
        CO2mask = CO2mask & (datarr[:,r] == CO2val)

    if (len(O2mask[O2mask == True]) == 1):
        O2done = True
    if (len(CO2mask[CO2mask == True]) == 1):
        CO2done = True

print('O2 done:',O2done)
print('CO2 done:',CO2done)

O2result = ''.join([str(i) for i in datarr[O2mask][0]])
CO2result = ''.join([str(i) for i in datarr[CO2mask][0]])

print(O2result,'=',int(O2result,2))
print(CO2result,'=',int(CO2result,2))
print(int(O2result,2)*int(CO2result,2))
