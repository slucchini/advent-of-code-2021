import numpy as np

called_numbers = np.loadtxt("data/Day4.txt",dtype=str,max_rows=1)
called_numbers = np.array(str(called_numbers).split(',')).astype(int)

boards = np.loadtxt("data/Day4.txt",skiprows=1)
boards_left = boards
boardsize = bz = 5
boards_marked = np.zeros(np.shape(boards))

boards_T = np.zeros(np.shape(boards))
boards_left_T = boards_T
boards_marked_T = np.zeros(np.shape(boards))
for i in range(int(len(boards)/bz)):
    boards_T[i*bz:(i+1)*bz] = boards[i*bz:(i+1)*bz].T

def reset():
    global boards_marked,boards_marked_T
    global boards_left,boards_left_T
    boards_marked = np.zeros(np.shape(boards))
    boards_marked_T = np.zeros(np.shape(boards))
    boards_left = boards
    boards_left_T = boards_T

def check_board(i):
    global boards_marked,bz
    b = boards_marked[i*bz:(i+1)*bz]
    check = np.concatenate((np.sum(b,axis=1),np.sum(b,axis=0)))
    if np.any(check == 5):
        return True
    else:
        return False

# bingo = False
# nboards = int(len(boards)/bz)
# reset()
# for i,n in enumerate(called_numbers):
#
#     boards_marked[boards == n] = 1
#     boards_marked_T[boards_T == n] = 1
#
#     for b in [boards_marked,boards_marked_T]:
#         if np.any(np.sum(b,axis=1) == bz):
#             bingo = True
#             board_number = int(np.where((np.sum(b,axis=1) == bz) == True)[0][0] / bz)
#             print("Bingo on {} for board #{}!".format(i,board_number))
#
#     if bingo:
#         break

# alternate method
print("Part 1")
bingo = False
nboards = int(len(boards)/bz)
board_number = None
reset()
for i,n in enumerate(called_numbers):

    boards_marked[boards == n] = 1
    boards_marked_T[boards_T == n] = 1

    for b in range(nboards):
        if (check_board(b)):
            bingo = True
            board_number = b
            print("Bingo on {} for board #{}!".format(i,b))
            break

    if bingo:
        break

winning_board = boards[board_number*boardsize:(board_number+1)*boardsize]
winning_marked = boards_marked[board_number*boardsize:(board_number+1)*boardsize]
sum_unmarked = np.sum(winning_board[np.invert(winning_marked.astype(bool))])
print("Score: {}".format(sum_unmarked*n))
print("")

# Part 2
print("Part 2")
bingo = False
nboards = int(len(boards)/bz)
board_number = None
reset()

boards_marked = np.ones(np.shape(boards))
boards_marked_T = np.ones(np.shape(boards))

for i,n in enumerate(called_numbers[::-1]):

    boards_marked[boards == n] = 0
    boards_marked_T[boards_T == n] = 0

    for b in range(nboards):
        if (not check_board(b)):
            bingo = True
            board_number = b
            print("Last bingo on {} for board #{}!".format(i,b))
            break

    if bingo:
        break

boards_marked[boards == n] = 1
boards_marked_T[boards_T == n] = 1

winning_board = boards[board_number*boardsize:(board_number+1)*boardsize]
winning_marked = boards_marked[board_number*boardsize:(board_number+1)*boardsize]
sum_unmarked = np.sum(winning_board[np.invert(winning_marked.astype(bool))])
print("Score: {}".format(sum_unmarked*n))
