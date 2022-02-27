# A
# N x N
# (1,1) (N,N)
# L R U D

# input example
# 2
# U U U U

# (rows, columns)
# rows, columns cannot be 0 or exceed N

# start point 1,1

from turtle import pos


moveDict = {"L":-1, "R":1, "U":-1, "D":+1}

square = int(input())
moveList = input().split()

position_x = 1
position_y = 1

for move in moveList:
    if(move == "L" or move == "R"):
        position_y += moveDict[move]
    if(move == "U" or move == "D"):
        position_x += moveDict[move]
    if(position_x == 0):
        position_x = 1
    if(position_y == 0):
        position_y = 1
    if(position_x > square):
        position_x = square
    if(position_y > square):
        position_y = square

    
print("%d %d" % (position_x,position_y))
        