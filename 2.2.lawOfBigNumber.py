input1 = "5 8 3"
input2 = "2 4 5 4 6"

# n: length of array
# m: counter of add number
# k: 

n, m, k = list(map(int, input1.split()))
numbers = list(map(int, input2.split()))
numbers.sort()
numbers.reverse()

big_1st = numbers[0]
big_2nd = numbers[1]
check = True

result = 0
countAdd = 0

while(countAdd < m):
    
    if(check):
        result += big_1st*3
        print(str(big_1st) * 3)
        check = not check
        countAdd += 3

    else:
        if(big_1st == big_2nd):
            result += big_2nd*3
            print(str(big_2nd) * 3)
            countAdd += 3
        else:
            result += big_2nd*1
            print(str(big_2nd) * 1)
            countAdd += 1

        check = not check

print(result)
