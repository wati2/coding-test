#11021번
T = int(input())

lis = []

for _ in range(T):
    lis.append(tuple(map(int,input().split(" "))))

for i, val in enumerate(lis):
    print("Case #%d: %d" % (i+1,sum(val)))