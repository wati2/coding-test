input_data = input()

row = int(input_data[1])
column = int(ord(input_data[1])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), (1,-2), (2,1), (1,2), (-1,2),(-2,1)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if (next_row > 0 and next_row <9 and next_column > 0 and next_column < 9):
        result += 1

print(result)