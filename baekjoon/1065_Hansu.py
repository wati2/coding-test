# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

# 양의정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다
# 등차수열은 연속된 두개의 수 차이가 일정한 수열을 말한다
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를
# 출력하는 프로그램을 작성하시오

# 111 은 한수
# 123 도 한수
# 2468 도 한수
# 1 도 한수 취급

# 차이가 일정한지 확인
def isHansu(x):
    lis = map(int,list(str(x)))
    checkDiff = None
    saveValue = None
    isHansu = True

    for n in lis:
        if saveValue == None:
            saveValue = n
        else:
            if checkDiff == None:
                checkDiff = n - saveValue
                # 다음계산에 사용
                saveValue = n
            elif checkDiff == (n - saveValue):
                # 다음계산에 사용
                saveValue = n
                continue
            else:
                # 한수가 아님
                return False

    return True

# 한수인 경우만 카운트
def countHansu(x):
    count = 0
    for i in range(1,x+1):
        if isHansu(i):
            count +=1

    return count

inValue = int(input())
print(countHansu((inValue)))