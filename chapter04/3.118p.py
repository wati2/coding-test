# <3> 실전문제. 게임개발
# N, M
# (A, B)

# 1. 반시계회전
# 2. 왼쪽방향 회전, 안가봤다면 한칸 이동
#    가봤다면, 다시 Step1 으로
# 3. 네칸 모두 가본 곳 or 바다이면 한칸 뒤로 후 Step1 으로
#    뒤로 갈 수가 없으면 멈춰야함
# 

# (3 <= N, M <= 50)
# 



from typing import Counter


directionDict = { 0:"북쪽", 1:"동쪽", 2:"남쪽", 3:"서쪽"}
charactorStep = { "북쪽":(0,-1), "동쪽":(1,0), "남쪽":(0,1), "서쪽":(-1,0)}
directionOrder = [0,3,2,1]

# 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다
# 맵의 외곽은 항상 바다로 되어있다
# 0:육지
# 1:바다
# 처음 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다

# Output 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다

print("전체 맵 크기 N M 입력")
input_map = list(map(int,input().split()))
max_row, max_col = input_map

print("캐릭터 상태값 입력 1 1 0")
input_status = list(map(int,input().split()))

row, col, direction = input_status
count = 0
counterRotate = 0
vMap = []
vMapExplore = {}

for in_row in range(max_row):
    print("%d Row 의 값 %d 개 입력 " % (int(in_row)+1,max_col))
    vMap.append(list(map(lambda x: True if x==1 else False, input().split())))




print("현재위치 (%d,%d) %s" % (row,col,directionDict[direction]))

# 현재 위치는 탐색된 것으로 간주
vMap[col][row] = True

while(True):
    next_row = row + charactorStep[directionDict[direction]][0]
    next_col = col + charactorStep[directionDict[direction]][1]

    if(next_row > 0 and next_row <= max_row and next_col > 0 and next_col <= max_col) and not vMap[next_col -1][next_row-1]:
        # 이동해도됨 이동
        row = next_row
        col = next_col

        print("다음칸 이동 (%d,%d)" % (row,col))
        # 이동 위치는 탐색된 것으로 간주
        vMap[col-1][row-1] = True
        count += 1
        counterRotate = 0
    else:
        # 좌로 회전
        direction = directionOrder[(directionOrder.index(direction) + 1) % 4]
        print("좌로회전 (%s)" % (directionDict[direction]))
        counterRotate += 1

    if counterRotate >=4:
        break


print(count)
