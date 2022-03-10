# n을 d(n) 의 생성자 라고함
# 입력 none
# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 
# 증가하는 순서로 출력한다

# 셀프넘버 = 생성자가 없는 숫자
# 생성될 수 없는 숫자

# 생성자가 있는지 없는지.. 어떻게?
# 1
# res = 1 + 1
# 피보나치 수열처럼 끝까지 가기

def d(n):
    # 33
    # res = 33 + 3 + 3
    # 제곱표현 x**y
    l = len(str(n))
    res = n

    for i in range(l):
        res += (n % (10**(i+1)))// (10**i)

    return res



lis = list(range(1,10001))
count = 0

while True:
    count += 1
    calculated = d(count)

    if calculated <= 10000:
        try:
            lis.remove(calculated)
        except:
            pass
    if count >= 11000:
        break

lis = list(set(lis))
lis.sort()

for i in lis:
    print(i)