# 출력 문자 %
# 출력 부동소수점

C = int(input())

S = []
Res = []

for _ in range(C):
    S.append(list(map(int,input().split(" "))))

for _ in S:
    N = _[0]
    Avg = sum(_[1:])/N

    count = 0
    for _ in _[1:]:
        if _ > Avg:
            count += 1
    
    Res.append(count/N * 100)

for _ in Res:
    print("%0.3f%%" % _)