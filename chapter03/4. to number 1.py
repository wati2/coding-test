
n, k = map(int, input().split())

counter = 0

while(True):
    counter += 1
    if (n == 1):
        break
    if (n % k == 0):
        n //= k
    else:
        n -= 1
        

print(counter)

# 25,5
# 5,5
# 1,5