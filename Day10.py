import numpy as np
from collections import deque

data = np.loadtxt("data/Day10.txt",dtype=str)

# Part 1
print("Part 1")

def get_type(c):
    if ((c == '(') | (c == ')')):
        return 'a'
    if ((c == '[') | (c == ']')):
        return 'b'
    if ((c == '{') | (c == '}')):
        return 'c'
    if ((c == '<') | (c == '>')):
        return 'd'

def is_open(c):
    if ((c == '(') | (c == '[') | (c == '{') | (c == '<')):
        return True
    else:
        return False

groups = deque()
errors = []
corrupted_lines = []
for i,d in enumerate(data):
    for c in list(d):
        if (is_open(c)):
            groups.append(c)
        else:
            if (get_type(c) == get_type(groups[-1])):
                groups.pop()
            else:
                errors.append(c)
                corrupted_lines.append(i)
                break

corrupted_lines = np.array(corrupted_lines)
errors = np.array(errors)
print(errors)

score = len(errors[errors == ')'])*3 + len(errors[errors == ']'])*57 + \
        len(errors[errors == '}'])*1197 + len(errors[errors == '>'])*25137
print(score)
print("")

# Part 2
print("Part 2")

# discard the corrupted lines
mask = np.ones(len(data),dtype=bool)
mask[corrupted_lines] = 0
data2 = data[mask]

def get_score(comp):
    score = 0
    for c in list(comp):
        score *= 5
        if (c == '('):
            score += 1
        elif (c == '['):
            score += 2
        elif (c == '{'):
            score += 3
        elif (c == '<'):
            score += 4
    return score

groups = deque()
completions = []
for i,d in enumerate(data2):
    for c in list(d):
        if (is_open(c)):
            groups.append(c)
        else:
            if (get_type(c) == get_type(groups[-1])):
                groups.pop()
            else:
                raise Exception("Unexpected.")
    completions.append(''.join(list(groups)[::-1]))
    groups = deque()

scores = np.array([get_score(c) for c in completions])
sscores = np.array(sorted(scores))
print("Middle score: {}".format(sscores[len(sscores)//2]))
