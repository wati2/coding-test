# 8 x 8
# Night, Moving like L
# x2 y1 or y2 x1

# position x : a,b,c,d,e,f,g,h
# position y : 1,2,3,4,5,6,7,8

# input : a1 or c2 or etc...
# output : can going to position, number of things

dictX = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}

# 1,2
# 2,1

input1 = input()

position_x, position_y = input1[0],input1[1]

position_x = dictX[position_x]
position_y = int(position_y)
counter = 0

for x in [1,-1,2,-2]:

    if(x == 1 or x == -1):
        case_y = [2,-2]
    if(x == 2 or x == -2):
        case_y = [1,-2]
    
    for y in case_y:
        if(0 < (position_x + x) and (position_x + x) <9 and 0 < (position_y + y) and (position_y + y) < 9):
            counter += 1 
        

    

print("%s, %s" %(position_x, position_y))
print(counter)