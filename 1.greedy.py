# 그리디
# 현 상황에서 지금 당장 좋은 것만 고르는 법


# infinite 500, 100, 10
# rest money is N won
# find minimum number of coin
# N is multiple of 10

n = 1260
coinSort = [500,100,50,10]
# coinDict = {}
count = 0

print(n)

for coin in coinSort:
    count += n // coin
    # coinDict[coin] = n // coin
    n %= coin

print(count)

# for sort, num in coinDict.items():
#     print("%d, %d" % (sort,num))

