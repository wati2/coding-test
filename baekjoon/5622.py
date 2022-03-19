"""  
ABC:1
DEF:2
GHI:3
...

숫자 1은 2초
A to Z
"""

inWord = list(input())

A_to_Z = list(map(chr,range(ord('A'),ord('Z')+1)))
phoneDict = {}
count = 0

for i in A_to_Z:
    phoneDict[i] = (count // 3) + 1
    count += 1

phoneDict["S"] -= 1
phoneDict["V"] -= 1
phoneDict["Y"] -= 1
phoneDict["Z"] -= 1

countTime = 0

for i in inWord:
    countTime += phoneDict[i] + 2

print(countTime)