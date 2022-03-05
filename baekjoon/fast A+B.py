import sys

n = int(input())
data = []

for _ in range(n):
    data.append(tuple(map(int, sys.stdin.readline().split(" "))))

for A,B in data:
    print(A+B)