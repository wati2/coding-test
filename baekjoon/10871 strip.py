N,X = list(map(int,input().split(" ")))
lis = list(map(int,input().split(" ")))

resultCollection = []

for i in lis:
    if i<X:
        resultCollection.append(i)

resultString = ""

for i in resultCollection:
    resultString += str(i) + " "

print(resultString.strip())